---
layout: page
title: Awards
---

<section>
  <ul>
  {% for award in site.awards reversed %}
    <li>
    <h2 class="award_title" onclick="showDiv('{{ award.name }}')">
      {{ award.rank }} at {{ award.name }} ({{ award.date-string }})
    </h2>

    <div id="{{ award.name }}" style='display: none'>

    {{ award.content | markdownify }}

    {% if award.image-team %}
      <h3 class="award_subtitle"></h3>
      <img src="{{ award.images-path }}{{ award.image-team }}" />
    {% endif %}


    {% if award.image-group %}
      <h3 class="award_subtitle">Teams:</h3>
      <img src="{{ award.images-path }}{{ award.image-group }}" />
    {% endif %}

    {% if award.image-scoreboard %}
      <h3 class="award_subtitle">Scoreboard:</h3>
      <img src="{{ award.images-path }}{{ award.image-scoreboard }}" />
    {% endif %}
    </div>
    <br>

    </li>

  {% endfor %}
  </ul>
</section>
