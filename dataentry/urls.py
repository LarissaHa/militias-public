from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('datasets/', views.datasets, name="datasets"),
    path('datasets/year_active/', views.year_active, name="year_active"),
    path('datasets/pgag_basic/', views.pgag_basic, name="pgag_basic"),
    path('imprint/', views.imprint, name="imprint"),
    path('privacy/', views.privacy, name="privacy"),
    # path('about-us/', views.about_us, name="about_us"),
    # path('more-info/', views.more_info, name="more_info"),
    path('country/', views.search_country, name="search_country"),
    path('countries/', views.country, name="country"),
    # path('regions/', views.regions, name="regions"),
    # path('regions/asia/', views.region_asia, name="region_asia"),
    # path('regions/africa/', views.region_africa, name="region_africa"),
    # path('regions/americas/', views.region_americas, name="region_americas"),
    # path('regions/europe/', views.region_europe, name="region_europe"),
    # path('regions/oceania/', views.region_oceania, name="region_oceania"),
    path('country/<int:country_id>/', views.new_country_detail, name='new_country_detail'),
    path('pgag/<int:pgag_id>/', views.detail_group, name='detail_group'),
    path('pgag/<int:pgag_id>/evidence/', views.pgag_evidence, name='pgag_evidence'),
    # path('groups/', views.groups, name="groups"),
    path('pgag/', views.search_pgag, name="search_pgag"),
    path('type/', views.type, name="type"),
    path('type/<type_name>/', views.type_generic, name="type_generic"),
    path('link/', views.link, name="link"),
    path('link/<int:link_id>/', views.link_detail, name="link_detail"),
    path('support/', views.support, name="support"),
    path('support/<int:support_id>/', views.support_detail, name="support_detail"),
    path('member/', views.member, name="member"),
    path('member/<int:member_id>/', views.member_detail, name="member_detail"),
    path('target/', views.target, name="target"),
    path('target/<int:target_id>/', views.target_detail, name="target_detail"),
    path('purpose/', views.purpose, name="purpose"),
    path('purpose/<int:purpose_id>/', views.purpose_detail, name="purpose_detail"),
    # path('entries/', views.index, name='index'),
    # path('entries/<int:target_id>/', views.detail, name='detail'),
    # path('entries/<int:target_id>/results/', views.results, name='results'),
    # path('entries/<int:target_id>/vote/', views.vote, name='vote'),
]