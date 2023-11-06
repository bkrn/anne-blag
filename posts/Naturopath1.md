---
title: Naturopath Post no. 1
author: Marianne
kind: post
---
# This is My First Map!

Hello and welcome to Anne Blag! The purpose of this blog is to give me a reason to keep practicing using tools like QGIS, slowly learn Python and SQL, and to explore topics that I am interested in. The posts on this blog are created by myself (with help from my partner Aaron). I use publicly available data and the posts are in no way representative of my employer. 

This post is the first in what will likely be a series of posts. The intent behind this project is to answer a few questions about Naturopathic Physicians in Washington state. Specifically, where are they located in Washington, and are they primarily in rural or urban areas across the state? The bigger question is, if their scope of practice was expanded - would they improve access to care in underserved rural areas?

To start to answer this question I first needed to find data sets. Luckily, Aaron was somehow able to find a list of providers and their addresses in Washington that bill Medicaid and Medicare (via NPI numbers). While I would be lost without him on these projects, and I am incredibly grateful for his help, I can’t help but be a little annoyed that he does not take me along for the full journey sometimes. As a result, I cannot provide the link to where we got the data from. But I promise it was publicly available on the internet somewhere.

Once we had the addresses of about 500 providers who bill Medicare and Medicaid in Washington, we could use QGIS to geolocate the addresses and get the latitude and longitude of each location. From there I added a point layer - each point is a physical address (really the latitude and longitude) of a Naturopathic Physician who has an NPI number (aka bills Medicare and Medicaid). This was laid over a map of Washington including boundaries of each county. But this just showed us where they were - it did not tell us anything about these areas. Are they urban areas? Rural areas? To answer this question I had to find another layer.

I found a [shapefile](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural.html) from the US Census Bureau’s website that provides a map of urban areas in Washington. This is part of a project by the Census Bureau that maps all of the urban-rural classification areas in the US. What is considered an urban area according to the US Census? Great question! Here is a great 7 minute video from the Census Bureau that explains it in detail:   https://www.census.gov/library/video/2022/defining-census-bureau-urban-areas.html. Now that I have mapped all of the locations of Naturopathic Physicians in Washington, I can use the shapefile from the US Census Bureau to delineate urban vs rural areas, and see how many Naturopathic Physicians are working in areas defined as urban versus rural areas. 

![image](/static/images/Naturopathmap1.png)

The map above indicates that the blue diamonds are rural area Naturopathic Physicians that bill Medicaid and Medicare - there are 21 total. Some of these areas are places that I personally would not consider rural. For example, Vashon and Port Townsend are very close to Seattle, you just need to take a ferry, but that is just my personal opinion. After I looked through the location of all 21 providers in rural areas, I found that about 9 are in areas that I would consider truly “rural”. Again, that’s just my personal opinion though. If you’re curious, here are the towns that the 21 “rural” providers are practicing in. Take a look and think if you’d consider these towns rural or not:

 1. Olga
 1. Kettle Falls
 1. Amboy
 1. Poulsbo
 1. Brewster
 1. Port Hadlock
 1. Arlington
 1. Neah Bay
 1. Camas
 1. Monroe
 1. Cashmere
 1. Snohomish
 1. Vashon
 1. Port Townsend
 1. Stevenson
 1. Eastsound
 1. Cusick
 1. Roy
 1. Carnation
 1. Belfair
 1. Randle 

Personally, I considered Olga, Kettle Falls, Amboy, Brewster, Neah Bay, Stevenson, Cusick, and Randle to be what I think of when I hear the word “rural”. 

Okay, now what?
So as I mentioned above, this is not a comprehensive list of all of the Naturopathic Physicians in Washington. This map only represents those providers that have an NPI number in order to bill Medicare and Medicaid. An interesting next step would be to see if I could find a data set with all Naturopathic Providers in Washington, to see if the map changes or not when factoring those who only accept private pay. Or maybe get a random sampling of private pay providers and build a model to test against to see if the two populations are different or not. This would be a good exercise to help me remember my Epi coursework…but also….maths. 🙁

To get closer to answering the question of “would expanding scope for Naturopathic Physicians help address rural healthcare access or not”, there are a few other things we could play with. We could put a 30 mile radius around providers to get a better picture (visually) of rural areas served by each provider. We could also do a population density calculation and visual representation. However, we would not want to do this with county level data as it’d be watered down across the large counties and basically meaningless. So to do something like this, we’d need to use census tracts or something similar. 

I’ll keep thinking about it and maybe come up with something new next time. Or I may pivot to a different topic!

Thanks for stopping by the Anne Blag.