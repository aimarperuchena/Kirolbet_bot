DELETE FROM `odds`
WHERE id>0;
alter table odds AUTO_INCREMENT =1;

DELETE FROM `game_bet`
WHERE id>0;
alter table game_bet AUTO_INCREMENT =1;

DELETE FROM `game`
WHERE id>0;
alter table game AUTO_INCREMENT =1;
DELETE FROM `market`
WHERE id>0;
alter table market AUTO_INCREMENT =1;
DELETE FROM `league`
WHERE id>0;
alter table league AUTO_INCREMENT =1;
DELETE FROM `sport`
WHERE id>0;
alter table sport AUTO_INCREMENT =1;


