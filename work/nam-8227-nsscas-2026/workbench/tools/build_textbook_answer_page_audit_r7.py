"""Apply the four named R7 observation repairs to the frozen accepted R6 audit."""
import json
from analysis_sources import A,WB,ROOT,digest,write
from apply_textbook_source_repairs_r7 import _read,apply_answer_page_audit


def main():
    baseline=_read()['answer_page_audit_r6_baseline'];path=ROOT/baseline['path']
    assert digest(path)==baseline['sha256'],'accepted R6 key-page audit baseline changed'
    result=apply_answer_page_audit(json.loads(path.read_text()),wb=WB)
    write(A/'textbook-answer-page-audit-r6.json',result)
    print('Applied4native-backed observation corrections and2key-locator additions;103original boundary regions retained.')


if __name__=='__main__':main()
