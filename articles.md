---
layout: page
title: Articles
---

<section>
  {% if site.posts[0] %}

    {% capture firstpostyear %}{{ site.posts[0].date | date: '%Y' }}{% endcapture %}
    <h3>{{ firstpostyear }}</h3>
    <ul>

    {% for post in site.posts %}
      {% if post.next %}
        {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
        {% capture nyear %}{{ post.next.date | date: '%Y' }}{% endcapture %}
        {% if year != nyear %}
          </ul>
          <h3>{{ post.date | date: '%Y' }}</h3>
          <ul>
        {% endif %}
      {% endif %}
      <li><time>{{ post.date | date: "%d %b" }}</time>
        <a href="{{ post.url | prepend: site.baseurl | replace: '//', '/' }}">
          {{ post.title }}
        </a>
      </li>
    {% endfor %}
    </ul>

  {% endif %}
</section>
