WITH domain_count AS (
    SELECT domain, COUNT(*) AS domain_frequency
    FROM "Users"
    GROUP BY domain
)
SELECT U.*
FROM "Users" U
JOIN "domain_count" DC ON U.domain = DC.domain
WHERE DC.domain_frequency = (
    SELECT MAX(domain_frequency) FROM domain_count
);
