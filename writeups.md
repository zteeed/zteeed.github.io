---
layout: page
title: Writeups
---

<section>
  <ul>
  {% for writeup in site.writeups reversed %}
    <li>
    <a href="{{ writeup.url | prepend: site.baseurl | replace: '//', '/' }}">
      {{ writeup.title }}
    </a>
    </li>
  {% endfor %}
  </ul>
</section>
