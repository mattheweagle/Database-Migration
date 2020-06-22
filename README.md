# Database-Migration

Seamlessly migrate the Yelp dataset from MongoDB to PostgreSQL on Amazon RDS

[Link to presentation slides](https://docs.google.com/presentation/d/1btjZ559A031FWwBrEUel30LVHatJSlC6ICJMF3SYW7k/edit?usp=sharing)

## Introduction

There are a lot of reasons a company might want to migrate their data from a self managed database cluster to an managed service like Amazon RDS. My project was inspired by a blog written by The Guardian that described their process for migrating all of their online content from MongoDB to PostgreSQL. That article can be found [here](https://www.theguardian.com/info/2018/nov/30/bye-bye-mongo-hello-postgres). Some existing migration tools only support relational to relational migration. In addition, businesses need a way to migrate their data without interuptions while requests continue to come in.

## Architecture

![Pipeline](images/pipeline.png)

## Engineering challenges
