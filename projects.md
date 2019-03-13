---
layout: page
title: Projects
---

<section>
  <ul>
  {% for project in site.projects reversed %}
    <li>
    <div>
      <img class="project_logo" src="{{ project.images-path }}{{ project.image-logo }}" />
      <h2 class="project_title" onclick="showDiv('{{ project.name }}')">
        {{ project.name }} ({{ project.date-string }})
      </h2>
    </div>

    <div id="{{ project.name }}" style='display: none'>

    {{ project.content | markdownify }}

    {% if project.website %}
      <h3 class="project_subtitle"></h3>
      Website: <a href="{{ project.website }}">{{ project.website }}</a>
    {% endif %}


    {% if project.github-link %}
      <h3 class="project_subtitle"></h3>
      Github project: <a href="{{ project.github-link }}">{{ project.github-link }}</a>
    {% endif %}

    </div>
    <br>

    </li>

  {% endfor %}
  </ul>
</section>
