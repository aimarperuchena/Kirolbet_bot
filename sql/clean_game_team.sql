DELETE FROM `game_team`
WHERE id>0;
alter table game_team AUTO_INCREMENT =1;
DELETE FROM `team`
WHERE id>0;
alter table team AUTO_INCREMENT =1;