create table if not exists accounts
(
    id         int auto_increment primary key,
    first_name varchar(100),
    last_name  varchar(100),
    birth_date timestamp,
    biography  text,
    picture_id varchar(100),
    email      varchar(100)
);

create table if not exists albums
(
    id           int auto_increment primary key,
    title        varchar(100),
    produce_time timestamp,
    genre        varchar(100)
);

create table if not exists singers
(
    id         int auto_increment primary key,
    first_name varchar(100),
    last_name  varchar(100),
    birth_date timestamp,
    biography  text,
    picture_id varchar(100),
    album_id   int,
    foreign key (album_id) references albums (id)
);

create table if not exists medias
(
    id           int auto_increment primary key,
    caption      varchar(500),
    media_name   varchar(100),
    produce_time timestamp,
    file_id      varchar(100),
    album_id     int,
    foreign key (album_id) references albums (id),
    unique (album_id, id)
);

create table if not exists likes
(
    account_id int,
    media_id   int,
    foreign key (account_id) references accounts (id),
    foreign key (media_id) references medias (id)
);

create table if not exists visit
(
    account_id int,
    media_id   int,
    foreign key (account_id) references accounts (id),
    foreign key (media_id) references medias (id)
);

create table if not exists follow
(
    account_id int,
    singer_id  int,
    foreign key (account_id) references accounts (id),
    foreign key (singer_id) references singers (id)
);