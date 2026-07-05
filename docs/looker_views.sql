-- Convenience views for Looker Studio.
-- The raw `date` columns are epoch nanoseconds (INT64, from Parquet load);
-- these views expose them as proper DATE so Looker's date controls work.
-- Run once:  bq query --use_legacy_sql=false < docs/looker_views.sql

CREATE OR REPLACE VIEW `steam_intel.v_game_daily` AS
SELECT appid,
       DATE(TIMESTAMP_SECONDS(DIV(date, 1000000000))) AS day,
       n, pos, neg, pos_rate, neg_rate
FROM `steam_intel.game_daily`;

CREATE OR REPLACE VIEW `steam_intel.v_alerts` AS
SELECT game, appid,
       DATE(TIMESTAMP_SECONDS(DIV(date, 1000000000))) AS day,
       n, neg_rate, base_neg_rate, z
FROM `steam_intel.alerts`;
