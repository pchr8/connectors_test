drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  name text not null,
  gender text,
  email text,
  age int,
  noshare boolean, 
  n1 int not null,
  nlist1 text,
  n2 int not null,
  nlist2 text,
  ip text not null,
  date int not null,
  comment text
);
