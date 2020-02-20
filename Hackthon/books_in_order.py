import numpy as np
import pandas as pd
import time
import os
import sys


def read_file(filename: str):
    with open(filename) as file:
        books_in_library_with_id = []
        nb_books_in_library_with_id = []
        signup_days_for_library_with_id = []
        shipping_speed_for_library_with_id = []
        
        for idx, line in enumerate(file):
            if(idx == 0):
                # Start of the file
                line_1 = line.replace('\n', '').split(' ')
#                 print(line_1)
                nb_books = int(line_1[0])
                nb_libraries = int(line_1[1])
                nb_days = int(line_1[2])

#                 print(nb_books)
#                 print(nb_libraries)
#                 print(nb_days)
            elif(idx == 1):
                book_scores_with_id = line.replace('\n', '').split(' ')
                book_scores_with_id = list(map(int,book_scores_with_id))

            else:

                if(idx % 2 == 0):
                    
                    #### Per library section
                    line_1 = line.replace('\n', '').split(' ')
                    if(line_1[0] == ''):
                        break

                    nb_books_in_library_with_id.append(int(line_1[0]))
                    signup_days_for_library_with_id.append(int(line_1[1]))
                    shipping_speed_for_library_with_id.append(int(line_1[2]))
                    
#                     print(nb_books_in_library_with_id)
#                     print(signup_days_for_library_with_id)
#                     print(shipping_speed_for_library_with_id)
                if(idx % 2 == 1):

                    book_ids = line.replace('\n', '').split(' ')
                    if(book_ids[0] == ''):
                        break

                    book_ids = list(map(int,book_ids))
                    books_in_library_with_id.append(book_ids)
#                     print("book ids : {}".format(books_in_library_with_id))



    return nb_books, \
            nb_libraries, \
            nb_days, \
            nb_books_in_library_with_id, \
            signup_days_for_library_with_id, \
            shipping_speed_for_library_with_id, \
            book_scores_with_id ,\
            books_in_library_with_id




def get_score_from_library(library_id : int, days_left : int, books_already_scanned : list):
    nb_books , \
    nb_libraries, \
    nb_days, \
    nb_books_in_library_with_id, \
    signup_days_for_library_with_id, \
    shipping_speed_for_library_with_id, \
    book_scores_with_id ,\
    books_in_library_with_id  = read_file("data/a_example.txt")

    # Update days left
    days_left = days_left - int(signup_days_for_library_with_id[library_id])

    # Compute books scanned and possible books in library to be used
    books = books_in_library_with_id[library_id]
    books_already_scanned_set = set(books_already_scanned)
    possible_books = set(books).difference(books_already_scanned_set)
    books_scanned = books_already_scanned_set.union(possible_books)

    # Compute score
    score = 0
    for book in possible_books:
        score += book_scores_with_id[book]

    return score, days_left, list(books_scanned)



def sort_books_per_library(library_list_in_order : list):

    nb_books , \
    nb_libraries, \
    nb_days, \
    nb_books_in_library_with_id, \
    signup_days_for_library_with_id, \
    shipping_speed_for_library_with_id, \
    book_scores_with_id ,\
    books_in_library_with_id  = read_file("data/a_example.txt")

    # Books IDs to send first of ALL books
    book_scores_index_sorted = list(reversed(sorted(range(len(book_scores_with_id)), key=book_scores_with_id.__getitem__)))

    book_shipping_sorted_for_library_with_id = []
    for library_id in library_list_in_order:
        books = books_in_library_with_id[library_id]

        shipping_order = []
        for book_id in book_scores_index_sorted:
            if(book_id in books):
                shipping_order.append(book_id)

        book_shipping_sorted_for_library_with_id.append(shipping_order)

    return book_shipping_sorted_for_library_with_id


if __name__ == '__main__':

    library_list_in_order = [0,1]

    book_shipping_sorted_for_library_with_id = sort_books_per_library(library_list_in_order)

    print(book_shipping_sorted_for_library_with_id)
