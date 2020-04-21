from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from .models import Course


@method_decorator(login_required, name='dispatch')
class CourseListView(ListView):

    model = Course
    template_name = 'courses/list.html'
    context_object_name = 'courses'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        courses = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(courses, self.paginate_by)
        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
            courses = paginator.page(1)
        except EmptyPage:
            courses = paginator.page(paginator.num_pages)
        context['course'] = courses
        return context

@method_decorator(login_required, name='dispatch')
class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/create.html'
    fields = ('title', 'description', 'language', 'abbreviation', 'ccode', 'major',  )
    success_url = reverse_lazy('course-list')


@method_decorator(login_required, name='dispatch')
class CourseDetailView(DetailView):

    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'courses'