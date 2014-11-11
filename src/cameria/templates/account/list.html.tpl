{% extends "partials/layout_account_l.html.tpl" %}
{% block title %}Accounts{% endblock %}
{% block name %}Accounts{% endblock %}
{% block content %}
    <ul class="filter" data-infinite="1" data-no_input="1">
        <div class="data-source" data-url="{{ url_for('list_accounts_json') }}" data-type="json" data-timeout="0"></div>
        <li class="template">
            <div class="name">
                <a href="{{ url_for('show_account', username = '') }}%[username]">%[username]</a>
            </div>
        </li>
        <div class="filter-no-results quote">
            No results found
        </div>
        <div class="filter-more">
            <span class="button more">Load more</span>
            <span class="button load">Loading</span>
        </div>
    </ul>
{% endblock %}
