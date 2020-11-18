from django.db import models

# Create your models here.
#第一轮面试结果
FIRST_INTERVIEW_RESULT_TYPE = ((u'建议复试',u'建议复试'), (u'待定',u'待定'), (u'放弃',u'放弃'))

#复试面试建议
INTERVIEW_RESULT_TYPE = ((u'建议录用',u'建议录用'), (u'待定',u'待定'), (u'放弃',u'放弃'))

#候选人学历
DEGREE_TYPE = ((u'本科',u'本科'), (u'硕士',u'硕士'), (u'博士',u'博士'))

#HR终面结论
HR_SCORE_TYPE = (('S','S'), ('A','A'), ('B','B'), ('C','C'))

class Candidate(models.Model):
    #基础信息
    userid = models.IntegerField(unique=True, blank=True, null=True,verbose_name=u'应聘者ID')
    username = models.CharField(max_length=135, verbose_name=u'姓名')

    #学校和学历信息
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=u'本科学校')
    major = models.CharField(max_length=135, blank=True, verbose_name=u'专业')
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=u'学历')

    #综合能力测评成绩，笔试测评成绩
    test_score_of_general_ability = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True, verbose_name=u'综合能力测评成绩')
    paper_score = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True, verbose_name=u'笔试成绩')

    #第一轮面试记录
    first_score =models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'初试分')

    #第二轮面试记录
    second_score =models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'复试分')

    #HR终面
    hr_score = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR综合复试等级')

    class Meta:
        db_table = u'candidate'
        verbose_name = u'应聘者'
        verbose_name_plural = u'应聘者'

    def __str__(self):
        return self.username