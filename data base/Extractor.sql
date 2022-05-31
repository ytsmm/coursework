SELECT t1.setting_value as doi, authors, year, number, t5.setting_value as title, t6.setting_value as abstract
FROM (
SELECT article_id, setting_value
FROM course.article_settings
WHERE setting_name = 'pub-id::doi'
) AS t1
LEFT JOIN (
SELECT submission_id, group_concat(CONCAT(SUBSTRING(authors.first_name,1,1), '. ', authors.last_name) SEPARATOR ', ') as authors
from course.authors
group by authors.submission_id
) AS t2
ON t1.article_id = t2.submission_id
LEFT JOIN (
SELECT article_id, SUBSTRING(date_published,1,4) as year
from course.published_articles
) AS t3
ON t1.article_id = t3.article_id
LEFT JOIN (
SELECT published_articles.article_id, CONCAT(issues.volume, '(', issues.number, '), pp. ', articles.pages) as number
FROM course.issues, course.published_articles, course.articles
WHERE published_articles.issue_id = issues.issue_id and published_articles.article_id = articles.article_id
) AS t4
ON t1.article_id = t4.article_id
LEFT JOIN (
SELECT article_id, setting_value
FROM course.article_settings
WHERE setting_name = 'cleanTitle'
) AS t5
ON t1.article_id = t5.article_id
LEFT JOIN (
SELECT article_id, setting_value
FROM course.article_settings
WHERE setting_name = 'abstract'
) AS t6
ON t1.article_id = t6.article_id
order by t1.article_id