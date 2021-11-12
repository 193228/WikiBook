import aiohttp
import asyncio
import time
key = "AIzaSyC49os9ZUxT05G7bTIXjQNw6AdoAobrtSg"

GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

async def get_book(session, url):
    async with session.get(url) as resp:
        book = await resp.json()
        return book

async def main(lista):
    retornoLista = []; urls = []
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(len(lista)):
            url = GOOGLE_BOOKS_URL+str(lista[i])+'&key='+str(key)
            print(url)
            urls.append(url)
            tasks.append(asyncio.ensure_future(get_book(session, url)))
        original_books = await asyncio.gather(*tasks)
        tiempoTranscurrido = time.time() - start_time
        print("<-- %s Tiempo transcurrido Usando concurrencia y asincrono -->" % (tiempoTranscurrido))
        retornoLista.append(original_books)
        retornoLista.append(tiempoTranscurrido)
        retornoLista.append(urls)
        return retornoLista


