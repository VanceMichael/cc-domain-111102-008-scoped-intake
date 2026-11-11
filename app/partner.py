from copy import deepcopy
import json
from pathlib import Path

class Partner:
    def __init__(self,root="fixtures"):
        root=Path(root)
        self.rows=json.loads((root/"observations.json").read_text())
        self.grants=json.loads((root/"grants.json").read_text())
        self.requests=[]
    def grant(self,purpose,revision=0):
        return deepcopy(self.grants[purpose][revision])
    def page(self,purpose,fields,scope,cursor=0,violate=False):
        self.requests.append({"purpose":purpose,"fields":list(fields),"scope":scope,"cursor":cursor})
        rows=self.rows[cursor:cursor+2]
        projected=[{k:v for k,v in r.items() if violate or k in fields} for r in rows]
        nxt=cursor+2 if cursor+2<len(self.rows) else None
        return {"scope":scope,"items":projected,"next_cursor":nxt}
