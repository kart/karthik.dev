---
layout: default
title: Home
---

# Karthik's Notes
Welcome to my personal engineering notebook.

## Latest Articles
<ul>
  {% for post in site.posts %}
    <li>
      <span>{{ post.date | date: "%b %d, %Y" }}</span>
      &raquo; 
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
