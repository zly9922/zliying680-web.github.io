#!/usr/bin/env python3
"""Create a review-only proposal from OpenAlex metadata; never auto-publish."""
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'papers.json'
REVIEW = ROOT / 'review' / 'PENDING_REVIEW.md'
TODAY = dt.datetime.now(dt.timezone.utc).date()
CUTOFF = (TODAY - dt.timedelta(days=120)).isoformat()
TOPICS = {
 '生成式推荐': [
   'generative recommendation semantic ID', 'residual quantization recommendation',
   'semantic identifier recommender system', 'codebook collapse quantization recommendation',
   'generative retrieval recommendation'],
 '金融市场': [
   'Trump financial markets', 'Trump social media stock market',
   'political speech gold oil prices', 'political communication financial volatility',
   'presidential statements market sentiment']
}
STRONG = {
 '生成式推荐': ['recommend','semantic id','semantic identifier','generative retrieval','quantiz','codebook','rq-vae','collaborative filter'],
 '金融市场': ['trump','president','presidential','political','speech','social media','tweet','truth social','financial market','gold price','oil price','crude oil']
}
WEAK = {'生成式推荐':['retrieval','recall','ranking','embedding','discrete code','muon'],
        '金融市场':['return','volatility','asset','stock','gold','oil','sentiment','event study','commodity','policy uncertainty']}
TAGS = {
 'Semantic ID':['semantic id','semantic identifier'], 'RQ-VAE':['rq-vae','residual quantization'],
 '码本稳定性':['codebook','collapse'], 'Muon':['muon'],
 '特朗普言论':['trump','truth social'], '黄金':['gold'], '原油':['oil','crude'],
 '市场情绪':['sentiment'], '事件研究':['event study']
}

def normalize(s): return re.sub(r'[^a-z0-9]+','',str(s).lower())

def abstract(inv):
    if not isinstance(inv,dict): return ''
    words=[]
    for token, positions in inv.items():
        if not isinstance(positions,list): continue
        words += [(pos,token) for pos in positions if isinstance(pos,int) and pos<10000]
    return ' '.join(w for _,w in sorted(words))[:2800]

def fetch(search):
    params={'search':search,'filter':f'from_publication_date:{CUTOFF},has_abstract:true',
            'per_page':'12','select':'id,doi,display_name,publication_year,publication_date,abstract_inverted_index,authorships,primary_location,type',
            'sort':'publication_date:desc'}
    key=os.getenv('OPENALEX_API_KEY','').strip()
    if key: params['api_key']=key
    url='https://api.openalex.org/works?'+urllib.parse.urlencode(params)
    req=urllib.request.Request(url,headers={'User-Agent':'AcademicPaperLibrary/1.0 (personal research discovery)','Accept':'application/json'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req,timeout=25) as response:
                return json.load(response).get('results',[])
        except (urllib.error.URLError,ValueError) as exc:
            print(f'OpenAlex search failed ({search}): {exc}',file=sys.stderr)
            if attempt<2: time.sleep(attempt+2)
    return []

def score(w,topic,ab):
    title=(w.get('display_name') or '').lower(); content=title+' '+ab.lower()
    # At least one strong keyword in title (or multiple in abstract), avoids broad false positives.
    title_hits=sum(s in title for s in STRONG[topic]); broad=sum(s in content for s in STRONG[topic]); weak=sum(s in content for s in WEAK[topic])
    if title_hits==0 and broad<2: return -1
    if topic=='金融市场' and not any(x in content for x in ['market','price','stock','asset','gold','oil','return','volatility','finance']):return -1
    if topic=='生成式推荐' and not any(x in content for x in ['recommend','retrieval','codebook','quantiz']):return -1
    return 4*title_hits+2*broad+min(weak,5)

def identifier(w):
    doi=(w.get('doi') or '').lower().strip().removeprefix('https://doi.org/')
    return 'doi:'+doi if doi else 'openalex:'+str(w.get('id','')).split('/')[-1].lower()

def record(w,topic,ab):
    title=w.get('display_name','').strip()
    authors=', '.join(x.get('author',{}).get('display_name','') for x in w.get('authorships',[])[:5])
    url=w.get('doi') or w.get('id') or ''
    lower=(title+' '+ab).lower()
    tags=[tag for tag,keys in TAGS.items() if any(k in lower for k in keys)]
    if topic=='生成式推荐' and not any(t in tags for t in ['Semantic ID','RQ-VAE','码本稳定性']): tags.append('生成式推荐')
    if topic=='金融市场' and not tags: tags.append('金融市场')
    return {'id':identifier(w),'title':title,'year':str(w.get('publication_year') or ''),'category':topic,
        'tags':tags[:6], 'summary':('英文摘要（未经过 AI 翻译）: '+ab[:1100]) if ab else '未提供摘要',
        'status':'待读','url':url if url.startswith('https://') else '',
        'notes':f"OpenAlex: {w.get('id','')}\n作者: {authors}\n发表日期: {w.get('publication_date','')}\n请审核论文真实性、研究相关性，并补充中文研究笔记。"}

def keys(p):
    allkeys={normalize(p.get('title',''))}
    doi=re.search(r'10\.\d{4,9}/[^\s]+',str(p.get('url','')),re.I)
    if doi: allkeys.add(normalize(doi.group(0)))
    allkeys.add(normalize(p.get('id','')))
    return allkeys-{''}

def main():
    if not DATA.exists(): raise SystemExit('papers.json not found. Do not create or overwrite your existing library.')
    original=json.loads(DATA.read_text(encoding='utf-8'))
    if not isinstance(original,list): raise SystemExit('papers.json must be an array')
    seen=set().union(*(keys(p) for p in original)) if original else set()
    selected=[]; report=[]; calls=0
    for topic, searches in TOPICS.items():
        ranked={}
        for query in searches:
            for w in fetch(query):
                ab=abstract(w.get('abstract_inverted_index')); title=w.get('display_name') or ''
                if not title or not ab:continue
                idkey=identifier(w); ntitle=normalize(title)
                if idkey in seen or ntitle in seen:continue
                s=score(w,topic,ab)
                if s<5:continue
                item=record(w,topic,ab)
                if idkey not in ranked or s>ranked[idkey][0]:ranked[idkey]=(s,item)
            calls+=1;time.sleep(0.35)
        best=sorted(ranked.values(),key=lambda x:(x[0],x[1]['year']),reverse=True)
        count=0
        for sc,item in best:
            if count>=5:break
            ident=keys(item)
            if seen & ident:continue
            seen.update(ident); selected.append(item);count+=1
            report.append(f"- **[{item['title']}]({item['url']})**（{item['year']}；{topic}；匹配分 {sc}）\n  - 标签：{', '.join(item['tags'])}\n  - {item['summary'][:430]}…")
        print(f'{topic}: {count} candidates')
    if selected:
        # Only append. Existing records and their annotations stay unchanged.
        DATA.write_text(json.dumps(original+selected,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        REVIEW.parent.mkdir(parents=True,exist_ok=True)
        REVIEW.write_text('# 待审核论文（免费元数据版本）\n\n'
                          f'运行日期：{TODAY.isoformat()}（UTC）\n\n'
                          '⚠️ **仅供人工审核；尚未公开发布。** 内容由 OpenAlex 元数据和关键词规则生成，'
                          '中文摘要没有自动翻译，请核实原文、日期、相关性并改写摘要。\n\n'
                          '审核时在 PR 的 Files changed 中核查 papers.json；移除不合适论文后再合并。\n\n'
                          + '\n\n'.join(report)+'\n',encoding='utf-8')
    else:
        print('No relevant new papers, leaving papers.json unchanged; no PR is necessary.')
if __name__=='__main__': main()
