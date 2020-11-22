from django.contrib import admin
from .models import Candidate
from django.http import HttpResponse
import csv
from datetime import datetime
import logging
from interview.dingtalk import send

# Register your models here.
logger = logging.getLogger(__name__)
exporttable_fields = ('username', 'bachelor_school')

def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    field_list = exporttable_fields
    response['Content-Disposition'] = 'attachment;filename=recuritment-candidates-list-%s.csv' % (
        datetime.now().strftime('%Y-%m-%d-%H'),
    )

    #写入表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list]
    )

    for obj in queryset:
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)
    logger.info("%s extend %s recores" %(request.user, len(queryset)))
    return response

#通知一面面试官
def notify_interviewer(modeladmin, request, queryset):
    candidates = ""
    interviewers = ""
    for obj in queryset:
        candidates = obj.username + "，" + candidates
    send("通知：候选人 {} 进入面试".format(candidates))

export_model_as_csv.short_description = u'导出为CSV文件'
notify_interviewer.short_description = u'通知一面面试官'

class CandidateAdmin(admin.ModelAdmin):
    #隐藏字段
    # exclude = ()
    #自定义导出到csv文件
    actions = [export_model_as_csv, notify_interviewer,]
    #展示字段
    # list_display = ()

    #查询字段
    search_fields = ('username',)

    #筛选条件
    list_filter = ('bachelor_school',)

    #排序
    ordering = ('hr_score',)

    #分组
    fieldsets = (
        (None, {'fields':("userid","username",("bachelor_school","major","degree"),("test_score_of_general_ability","paper_score"),)}),
        ('第一轮面试记录', {'fields':("first_score",)}),
        ('第二轮面试记录', {'fields':("second_score",)}),
        ('HR终面', {'fields':("hr_score",)}),
    )

admin.site.register(Candidate, CandidateAdmin)