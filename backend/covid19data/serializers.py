from rest_framework import serializers
from .models import *


# 코로나 일반 현황
class Covid19InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19Info
        fields = [
            "seq",  # ID
            "stateDt",  # 기준 일
            "stateTime",  # 기준 시간
            "createDt",  # 등록일시분초
            "accExamCnt",  # 누적 검사 수
            "examCnt",  # 검사 진행 수
            "accExamCompCnt",  # 누적 검사 완료 수
            "resutlNegCnt",  # 결과 음성 수
            "decideCnt",  # 확진자 수
            "careCnt",  # 치료중 환자 수
            "clearCnt",  # 격리해제 수
            "accDefRate",  # 누적 확진률
            "deathCnt",  # 사망자 수
            "updateDt",  # 수정일시분초(잘 사용하지 않음)
        ]


# 코로나 성별", 연령별 현황
class Covid19GenAgeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19GenAgeInfo
        fields = [
            "seq",  # ID
            "createDt",  # 등록일시분초
            "gubun",  # 구분(성별",연령)
            "confCase",  # 확진자
            "confCaseRate",  # 확진률
            "death",  # 사망자
            "criticalRate",  # 치명률 사망/확진*100
            "deathRate",  # 사망률(연령별", 성별별)
            "updateDt",  # 수정일시분초(잘 사용하지 않음)
        ]


# 코로나 지역별 현황
class Covid19SidoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19SidoInfo
        fields = [
            "seq",  # ID
            "stdDay",  # 기준일시
            "createDt",  # 등록일시분초
            "gubun",  # 구분(지역별)
            "gubunCn",  # 구분 한자
            "gubunEn",  # 구분 영어
            "defCnt",  # 확진자 수
            "isolIngCnt",  # 격리중 환자 수
            "isolClearCnt",  # 격리해제수
            "incDec",  # 전일대비증감수
            "deathCnt",  # 사망자 수
            "localOccCnt",  # 지역발생수
            "overFlowCnt",  # 해외유입수
            "qurRate",  # 10만명당발생률
            "updateDt",  # 수정일시분초(잘 사용하지 않음)
        ]
