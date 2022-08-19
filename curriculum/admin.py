from django.contrib import admin
from curriculum.models import Assignment, Standard, Subject, Lesson, Comment, Reply, Submission
# WorkingDays, TimeSlots, SlotSubject
# Register your models here.


admin.site.register(Standard)
# admin.site.register(Subject)
# admin.site.register(Comment)
# admin.site.register(Reply)
# admin.site.register(Assignment)
# admin.site.register(Submission)


# admin.site.register(WorkingDays)
# admin.site.register(TimeSlots)
# admin.site.register(SlotSubject)


class SubjectAdmin(admin.ModelAdmin):
	list_display = ('subject_id','name', 'standard',)
	search_fields = ('subject_id','name',)
	list_display_links = ('subject_id','name',)
admin.site.register(Subject, SubjectAdmin)

class LessonAdmin(admin.ModelAdmin):
	list_display = ('lesson_id','name', 'subject','Standard',)
	search_fields = ('name',)
	list_display_links = ('lesson_id','name','subject','Standard',)
admin.site.register(Lesson, LessonAdmin)


class CommentAdmin(admin.ModelAdmin):
	list_display = ('comm_name','author', 'body','lesson_name',)
	search_fields = ('comm_name','author', 'body','lesson_name', )
	list_display_links = ('comm_name','author', 'body',)
admin.site.register(Comment, CommentAdmin)

class ReplyAdmin(admin.ModelAdmin):
	list_display = ('comment_name','author', 'reply_body',)
	search_fields = ('comment_name','author', 'reply_body', )
	list_display_links = ('comment_name','author', 'reply_body',)
admin.site.register(Reply, ReplyAdmin)

class AssignmentAdmin(admin.ModelAdmin):
	list_display = ('title','description', 'lesson','file','post_time',)
	search_fields = ('title', 'description')
	list_display_links = ('title',)
admin.site.register(Assignment, AssignmentAdmin)


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment','description','file','user',)
    search_fields = ('assignment','user')
    list_display_links = ('assignment','user','description',)
admin.site.register(Submission, SubmissionAdmin)