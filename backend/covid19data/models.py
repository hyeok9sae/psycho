from django.db import models


class Covid19Info(models.Model):  # 코로나 일반 현황
    seq = models.IntegerField(primary_key=True)  # ID
    stateDt = models.CharField(max_length=200, null=True)  # 기준 일
    stateTime = models.CharField(max_length=200, null=True)  # 기준 시간
    createDt = models.DateTimeField(null=True)  # 등록일시분초
    accExamCnt = models.CharField(max_length=200, null=True)  # 누적 검사 수
    examCnt = models.CharField(max_length=200, null=True)  # 검사 진행 수
    accExamCompCnt = models.CharField(max_length=200, null=True)  # 누적 검사 완료 수
    resutlNegCnt = models.CharField(max_length=200, null=True)  # 결과 음성 수
    decideCnt = models.CharField(max_length=200, null=True)  # 확진자 수
    careCnt = models.CharField(max_length=200, null=True)  # 치료중 환자 수
    clearCnt = models.CharField(max_length=200, null=True)  # 격리해제 수
    accDefRate = models.CharField(max_length=200, null=True)  # 누적 확진률
    deathCnt = models.CharField(max_length=200, null=True)  # 사망자 수
    updateDt = models.CharField(max_length=200, null=True)  # 수정일시분초(잘 사용하지 않음)


class Covid19GenAgeInfo(models.Model):  # 코로나 성별, 연령별 현황
    seq = models.IntegerField(primary_key=True)  # ID
    createDt = models.DateTimeField(null=True)  # 등록일시분초
    gubun = models.CharField(max_length=200, null=True)  # 구분(성별,연령)
    confCase = models.CharField(max_length=200, null=True)  # 확진자
    confCaseRate = models.CharField(max_length=200, null=True)  # 확진률
    death = models.CharField(max_length=200, null=True)  # 사망자
    criticalRate = models.CharField(max_length=200, null=True)  # 치명률 사망/확진*100
    deathRate = models.CharField(max_length=200, null=True)  # 사망률(연령별, 성별별)
    updateDt = models.CharField(max_length=200, null=True)  # 수정일시분초(잘 사용하지 않음)


class Covid19SidoInfo(models.Model):  # 코로나 지역별 현황
    seq = models.IntegerField(primary_key=True)  # ID
    stdDay = models.CharField(max_length=200, null=True)  # 기준일시
    createDt = models.DateTimeField(null=True)  # 등록일시분초
    gubun = models.CharField(max_length=200, null=True)  # 구분(지역별)
    gubunCn = models.CharField(max_length=200, null=True)  # 구분 한자
    gubunEn = models.CharField(max_length=200, null=True)  # 구분 영어
    defCnt = models.CharField(max_length=200, null=True)  # 확진자 수
    isolIngCnt = models.CharField(max_length=200, null=True)  # 격리중 환자 수
    isolClearCnt = models.CharField(max_length=200, null=True)  # 격리해제수
    incDec = models.CharField(max_length=200, null=True)  # 전일대비증감수
    deathCnt = models.CharField(max_length=200, null=True)  # 사망자 수
    localOccCnt = models.CharField(max_length=200, null=True)  # 지역발생수
    overFlowCnt = models.CharField(max_length=200, null=True)  # 해외유입수
    qurRate = models.CharField(max_length=200, null=True)  # 10만명당발생률
    updateDt = models.CharField(max_length=200, null=True)  # 수정일시분초(잘 사용하지 않음)

# class Store(models.Model):
#     id = models.IntegerField(primary_key=True)
#     store_name = models.CharField(max_length=50)
#     branch = models.CharField(max_length=20, null=True)
#     area = models.CharField(max_length=50, null=True)
#     tel = models.CharField(max_length=20, null=True)
#     address = models.CharField(max_length=200, null=True)
#     latitude = models.FloatField(max_length=10, null=True)
#     longitude = models.FloatField(max_length=10, null=True)
#     category = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return [self.id, self.store_name, self.branch, self.area, self.address]

#     @property
#     def category_list(self):
#         return self.category.split("|") if self.category else []
