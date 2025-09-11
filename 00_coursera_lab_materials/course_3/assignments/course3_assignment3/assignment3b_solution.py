import requests
import requests_with_caching
import json

requests_with_caching.clear_cache()

BASIC_URL = "http://www.omdbapi.com/"
MY_API_KEY = "17949cd0"

BASIC_JOKE_URL = "https://icanhazdadjoke.com/search"


def get_movie_data(name: str) -> dict:
    try:
        query_param = {
            "t": name,
            "r": "json",
            "apikey": MY_API_KEY
        }
        response = requests_with_caching.get(BASIC_URL, query_param)

        movie_data = response.json()
        return movie_data

    except requests.exceptions.RequestException as e:
        print(f"\nThere is error on communication with server: {e}")
        return {}
    except json.JSONDecodeError:
        print("\nERROR: Server did not return valid JSON.")
        return {}


def rt_rating(movie_data: dict) -> int:
    ratings_list = movie_data["Ratings"]
    rating = -1
    for item in ratings_list:
        if item.get("Source") == "Rotten Tomatoes":
            value = item.get("Value")
            clean_value_int = int(value.replace("%", ""))
            rating = clean_value_int
    return rating


def get_joke_data(sinonym_word: str) -> dict:
    try:
        header_query = {
            "Accept": "application/json"
        }

        query_para = {
            "term": sinonym_word,
            "limit": 2
        }

        response = requests_with_caching.get(BASIC_JOKE_URL, query_para)
        joke_data = response.json()
        return joke_data

    except requests.exceptions.RequestException as e:
        print(f"\nThere is error on communication with server: {e}")
        return {}
    except json.JSONDecodeError:
        print("\nERROR: Server did not return valid JSON.")
        return {}


def get_jokes(plot: str, verbosity=0) -> tuple[str, list[str]]:
    words = plot.split()
    words = [w.strip(",.!;:") for w in words]
    sorted_words_list = sorted(words, key=lambda word: len(word), reverse=True)

    for sorted_word in sorted_words_list:
        dict_data = get_joke_data(sorted_word)

        if dict_data['results']:
            return sorted_word, [item['joke'] for item in dict_data['results']]
    return "", []


def highlight(word: str, sentence: str) -> str:
    import re
    return re.sub(re.escape(word), f"**{word}**", sentence, flags=re.IGNORECASE)


def haha_me(movie_title: str, verbosity=0) -> str:
    movie_info = get_movie_data(movie_title)
    if not movie_info or movie_info.get('Response') == 'False':
        return f"No movie found: {movie_title}"

    title = movie_info.get("Title", "Unknown Title")
    plot_summary = movie_info.get("Plot", "")
    movie_rate = rt_rating(movie_info)

    joke_word, jokes_list = get_jokes(plot_summary, verbosity)

    if not joke_word:
        return "I've got no jokes about this movie. It's too serious!"

    rating_string = f"Rotten Tomatoes rating: {movie_rate}%"
    highlighted_plot = highlight(joke_word, plot_summary)
    joke_intro_line = f"Speaking of **{joke_word}**, that reminds me of some jokes."

    joke_quality_line = ""
    if movie_rate == -1:
        joke_quality_line = "Hope you like them!"
    elif movie_rate < 70:
        joke_quality_line = "Hope they're better than the movie!"
    else:
        joke_quality_line = "Hope they're as good as the movie!"

    highlighted_jokes = [highlight(joke_word, joke) for joke in jokes_list]
    formatted_jokes = "\n".join(highlighted_jokes)

    final_output = (
            title + "\n" +
            rating_string + "\n" +
            highlighted_plot + "\n" +
            joke_intro_line + "\n" +
            joke_quality_line + "\n" +
            "\n" +
            formatted_jokes
    )

    return final_output

output = haha_me("Black Panther")
print(output)

