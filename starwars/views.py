from django.shortcuts import render
import requests
import json


url = "https://swapi-graphql-integracion-t3.herokuapp.com/"
headers = { 'Content-Type': 'application/json' }


def movies_list(request):
    query = {"query": '{ allFilms { edges { node {id title director producers releaseDate episodeID} } } }'}
    movies = requests.post(url, json=query, headers=headers).json()["data"]["allFilms"]["edges"]

    return render(request, 'movies_list.html', {'movies': movies})


def movie_info(request, movieId):
    query = {"query": '{{ film(id: "{}") {{ id title director producers releaseDate episodeID openingCrawl characterConnection {{ characters {{ name id }} }} starshipConnection {{ starships {{ name id }} }} planetConnection {{ planets {{ name id }} }} }} }}'.format(movieId)}
    movie = requests.post(url, json=query, headers=headers).json()["data"]["film"]

    return render(request, 'movie_info.html', {'movie': movie})


def planet_info(request, planetId):
    query = {"query": '{{ planet(id: "{}") {{ id name climates diameter gravity orbitalPeriod population rotationPeriod surfaceWater terrains filmConnection {{ films {{ id title }} }} residentConnection {{ residents {{ id name }} }} }} }}'.format(planetId)}
    planet = requests.post(url, json=query, headers=headers).json()["data"]["planet"]

    return render(request, 'planet_info.html', {'planet': planet})


def character_info(request, characterId):
    query = {"query": '{{ person(id: "{}") {{ id name birthYear eyeColor gender hairColor height mass skinColor homeworld {{ id name }} filmConnection {{ films {{ id title }} }} starshipConnection {{ starships {{ id name }} }} }} }}'.format(characterId)}
    character = requests.post(url, json=query, headers=headers).json()["data"]["person"]

    return render(request, 'character_info.html', {'character': character})


def ship_info(request, shipId):
    query = {"query": '{{ starship(id: "{}") {{ id name model starshipClass manufacturers costInCredits length crew passengers maxAtmospheringSpeed hyperdriveRating MGLT cargoCapacity consumables filmConnection {{ films {{ id title }} }} pilotConnection {{ pilots {{ id name }} }} }} }}'.format(shipId)}
    ship = requests.post(url, json=query, headers=headers).json()["data"]["starship"]

    return render(request, 'ship_info.html', {'ship': ship})

