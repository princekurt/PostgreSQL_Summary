#!/usr/bin python2.7
# Author Kurt Anderson
# Last Edited 5/25/2017

import psycopg2

DBNAME = "news"


def main():
    """Runs 3 query operations to print out a status report"""

    # Runs the Most Popular Articles Query
    print("\nMost Popular Articles\n")
    popular_articles = popular_articles_log()
    for x in range(0, len(popular_articles)):
        print(popular_articles[x][0] +
              " -- " +
              str(popular_articles[x][1]) +
              " views")
    # Runs the Most Popular Authors Query
    print("\nMost Popular Authors\n")
    popular_authors = popular_authors_log()
    for y in range(0, len(popular_authors)):
        print(popular_authors[y][0] +
              " -- " +
              str(popular_authors[y][1]) +
              " views")

    # Runs the Error Analysis
    print("\nDays with more than 1% request errors\n")
    errors = error_analysis()
    for z in range(0, len(errors)):
        print(str(errors[z][0]) + " -- " + str(errors[z][1]) + "%")
    print("\n")


def popular_articles_log():
    """Provides a query to return the most popular articles"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("WITH log AS ("
              " SELECT regexp_replace(log.path, '^.+[/\\\]','') AS logArticle "
              "FROM log ) "
              "SELECT articles.title, count(log.logArticle) as views "
              "FROM articles LEFT JOIN log "
              "ON articles.slug = logArticle "
              "GROUP BY articles.title "
              "ORDER BY views desc "
              "LIMIT 3")
    articles = c.fetchall()
    db.close()
    return articles


def popular_authors_log():
    """Performs a query to return the most popular authors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("WITH log AS ("
              " SELECT regexp_replace(log.path, '^.+[/\\\]','') AS logArticle "
              "FROM log ) "
              "SELECT authors.name, COUNT(log.logArticle) AS views "
              "FROM articles LEFT JOIN log "
              "ON articles.slug = logArticle "
              "JOIN authors "
              "ON articles.author = authors.id "
              "GROUP BY authors.name "
              "ORDER BY views desc ")
    authors = c.fetchall()
    db.close()
    return authors


def error_analysis():
    """Performs a query to return any days with erros over 1%."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT dates, ROUND(reports,2) FROM ("
              " SELECT "
              " CAST(log.time AS DATE) AS dates, "
              " SUM(CASE WHEN CAST(left(log.status, 1) AS INTEGER) "
              "     BETWEEN 4 AND 6 THEN 1 ELSE 0 END) * 100.0 /  " 
              "     COUNT(CAST(log.time as DATE)) AS reports "
              " FROM log "
              " GROUP BY dates "
              " ORDER BY reports desc ) AS aggregations "
              "WHERE reports >=1")
    errors = c.fetchall()
    db.close()
    return errors


if __name__ == '__main__':
    main()
