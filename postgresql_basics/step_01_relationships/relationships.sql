-- -- create database testdb;
--
drop table if exists publisher;
drop table if exists book;

create table if not exists publisher (
    publisher_id serial primary key ,
    org_name varchar(128) not null ,
    address text not null
);

create table if not exists book (
    book_id serial primary key ,
    title text not null ,
    isbn varchar(32) not null
);

alter table public.publisher
owner to postgres;


-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- One to Many  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


-- insert into book (title, isbn) values ('The Diary of a young girl', '019953566');
-- insert into book (title, isbn) values ('The Diary of a young girl2', '019953566');
-- insert into book (title, isbn) values ('The Diary of a young girl3', '019953566');

insert into book (title, isbn) values
                                      ('The Diary of a young girl4', '019953566'),
                                      ('The Diary of a young girl5', '019953566'),
                                      ('The Diary of a young girl6', '019953566'),
                                      ('The Diary of a young girl7', '019953566'),
                                      ('The Diary of a young girl8', '019953566')
                                      ;


insert into publisher (org_name, address) values
                                                 ('company1', 'Moscow, asdfkjhsdf'),
                                                 ('company2', 'Moscow, asdfkjhsdf'),
                                                 ('company3', 'Moscow, asdfkjhsdf'),
                                                 ('company4', 'Moscow, asdfkjhsdf'),
                                                 ('company5', 'Moscow, asdfkjhsdf')
                                                 ;

-- select * from book;
-- select * from publisher;

alter table book rename column book_id to id;
alter table publisher rename column publisher_id to id;

alter table book add column fk_publisher_id smallint;
alter table book add constraint fk_publisher_id foreign key (fk_publisher_id) references publisher (id);

-- fk can be created while table creating:

drop table if exists book;

create table if not exists book (
    book_id serial primary key ,
    title text not null ,
    isbn varchar(32) not null,
    fk_publisher_id integer references publisher(id) not null
);

insert into book (title, isbn, fk_publisher_id) values
                                      ('The Diary of a young girl1', '019953566', 1),
                                      ('The Diary of a young girl2', '019953566', 1),
                                      ('The Diary of a young girl3', '019953566', 1),
                                      ('The Diary of a young girl4', '019953566', 1)
                                      ;

insert into book (title, isbn, fk_publisher_id) values
                                      ('book1', '019953566', 1),
                                      ('book2', '019953563', 2),
                                      ('book3', '019953563', 2),
                                      ('book4', '019953563', 2)
                                      ;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- One to One -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

create table person (
    id int primary key,
    first_name varchar(50) not null ,
    second_name varchar(50) not null
);

create table passport (
    id int primary key,
    number int not null ,
    fk_person_id int references person(id)
);

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- Many to Many -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- drop table if exists publisher;
-- drop table if exists book;

create table if not exists book (
    id serial primary key,
    title text not null,
    isbn text not null
);

create table if not exists author (
    id serial primary key,
    name varchar(20) not null
);

create table if not exists book_author_rel (
    book_id int references book(id),
    author_id int references author(id),
    constraint book_author_pk primary key (book_id, author_id) -- composite key
);

insert into book (title, isbn) values
                                      ('book1', 'author1'),
                                      ('book2', 'author2'),
                                      ('book3', 'author3'),
                                      ('book4', 'author4')
                                      ;
insert into author (name) values
                                ('name1'),
                                ('name2'),
                                ('name3'),
                                ('name4')
                                ;
insert into book_author_rel values
                                   (1, 1),
                                   (1, 2),
                                   (1, 3),
                                   (2, 2),
                                   (2, 3),
                                   (3, 2),
                                   (3, 3),
                                   (3, 4)
                                   ;

