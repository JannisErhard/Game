#!/usr/bin/env python3
campaign = {}
campaign[1] = [
            list('SX#  EDE '),
            list('CC# EEEEE'),
            list('#-#     X'),
            list('         '),
            list('^       K'),
        ]

campaign[4] = [['K', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 'X', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '>', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', 'S', '#', ' ', ' ', 'D', ' ', ' '],
[' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', 'E', ' ', 'E', ' '],
['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '-', '#', '#'],
[' ', ' ', ' ', ' ', ' ', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', 'E', 'E', ' '],
[' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', 'E', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', 'E', '#', '#', 'E', '#', '#', ' ', ' ', ' ', ' ', ' ', ' '], 
[' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', 'E', 'S', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', 'K', '#', ' ', ' ', ' ', ' ', ' ', ' '], 
[' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', 'E', 'E', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 'H', ' ', ' ', ' ', '#', '#', 'E', '#', '#', 'E', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ']]
campaign[2] = [
['S',' ',' ',' ',' ',' ',' ','#',' '],
[' ',' ','#','#','#','#',' ','|','D'],
[' ',' ','E',' ',' ','#',' ','#',' '],
['#','#','#','#','E','#',' ','#','#'],
[' ',' ',' ',' ',' ','#',' ','E',' '],
['^',' ','E',' ',' ','E','K','E','X']]
campaign[6] = [
['S',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ','D'],
[' ',' ','E',' ',' ',' ',' ',' ',' '],
[' ',' ',' ','#','E',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ','E',' '],
['^',' ','E',' ',' ','E','K','E','X']]
campaign[3] = [
[' ',' ',' ','#','H','#','E','E','K'],
[' ','#','E','#',' ','#',' ','E','E'],
[' ','#',' ',' ',' ','|',' ',' ','E'],
[' ','#','#','#',' ','#','#','#','-'],
[' ','K','S','#',' ','#','D','E',' '],
['E','E','E','#','^','#','E',' ',' ']]
campaign[5] = [
['E',' ', 'E', ' ', 'E', 'E', 'E', ' ', 'E', ' ', ' ', 'E', ' ', '^', ' ', 'E', 'E', 'E'],
['E',' ', 'E', ' ', 'E', ' ', ' ', ' ', 'E', ' ', ' ', 'E', ' ', ' ', ' ', 'E', ' ', 'E'],
['E','E', 'E', ' ', 'E', 'E', ' ', ' ', 'E', ' ', ' ', 'E', ' ', ' ', ' ', 'E', 'D', 'E'],
['E',' ', 'E', ' ', 'E', ' ', ' ', ' ', 'E', ' ', ' ', 'E', ' ', ' ', ' ', 'E', ' ', 'E'],
['E',' ', 'E', ' ', 'E', 'E', 'E', ' ', 'E', 'E', ' ', 'E', 'E', ' ', ' ', 'E', 'E', 'E']]
campaign['empty'] = [
[' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' '],
['^',' ',' ',' ',' ',' ',' ',' ',' ']]
campaign[7]=[[' ', '4', ' ', '4', ' ', ' ', ' ', '16', '18', ' ', '6', ' ', ' ', '16', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', '5', '11', ' ', '1', ' ', '4', ' ', ' ', ' ', ' ', ' ', ' ', '5', '14', '3', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', '4', ' ', '#'], ['#', '3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '5', '9', ' ', '1', ' ', ' ', ' ', ' ', '1', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', '2', ' ', ' ', ' ', ' ', '10', '3', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', '4', ' ', ' ', '5', '3', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' '], [' ', '2', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '5', '9', ' ', ' ', ' ', '1', ' ', ' '], ['#', '12', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', '5', '3', ' ', ' ', ' ', ' ', ' ', ' ', '4', ' ', '1', ' ', ' ', ' ', '#'], ['#', '18', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', '1', ' ', '1', ' ', '1', ' ', '1', ' ', '2', ' ', '1', ' ', ' '], ['#', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '5', '15', '3', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '4', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', '1', ' ', '#'], [' ', '1', ' ', '5', '3', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', '1', ' ', '2', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', '1', ' ', '5', '9', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', '8', '11', ' '], [' ', '1', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '6', ' ', ' ', ' ', ' ', ' ', '5', '7', '3', ' ', ' ', '4', ' ', ' '], ['#', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', '6', ' ', '1', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', '1', ' ', ' ', '1', ' ', ' ', ' ', '1', ' ', '4', ' ', ' ', '5', '9', ' ', '1', ' ', '1', ' ', '5', '3', ' ', '#'], [' ', '1', ' ', '1', ' ', ' ', '2', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', '6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], [' ', ' ', ' ', ' ', ' ', ' ', '10', '3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '10', '9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], [' ', '8', '3', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '10', '7', '7', '3', ' ', '1', ' ', ' ', '#'], ['#', '11', ' ', '2', ' ', ' ', ' ', ' ', '5', '3', ' ', '1', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '4', ' ', ' ', '1', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', '5', '9', ' ', ' ', '8', '#'], ['#', '7', '3', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '6', ' ', ' ', '4', ' '], [' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ']]




campaign[8]=[['#', ' ', ' ', '#', '#', '#', '18', ' ', '16', '23', '#', '18', ' ', ' ', '16', '23', '18', ' ', '#', '18', ' ', ' ', '16', '23', '#'], ['#', '3', ' ', '25', '23', '18', ' ', ' ', ' ', ' ', '6', ' ', '2', ' ', ' ', ' ', ' ', '5', '11', ' ', '5', '3', ' ', ' ', '#'], [' ', ' ', '5', '11', ' ', ' ', ' ', ' ', ' ', '8', '15', '28', '26', ' ', ' ', '17', '19', ' ', ' ', ' ', ' ', ' ', '5', '3', ' '], ['#', ' ', ' ', ' ', '5', '9', ' ', ' ', '8', '11', ' ', '16', '31', '3', ' ', '25', '18', ' ', ' ', '1', ' ', '2', ' ', ' ', ' '], ['#', ' ', ' ', '2', ' ', '6', ' ', ' ', '6', ' ', ' ', ' ', ' ', ' ', '8', '11', ' ', ' ', ' ', ' ', ' ', '24', '19', ' ', '#'], ['#', '7', '28', '26', ' ', '4', ' ', '8', '15', '7', '7', '7', '3', ' ', '6', ' ', '1', ' ', ' ', '5', '28', '#', '18', ' ', ' '], ['#', ' ', '25', '18', ' ', ' ', '17', '26', ' ', ' ', ' ', ' ', ' ', '5', '11', ' ', ' ', ' ', ' ', ' ', '25', '18', ' ', ' ', '#'], ['#', ' ', '6', ' ', ' ', ' ', '16', '31', '9', ' ', '5', '28', '19', ' ', ' ', ' ', ' ', '8', '3', ' ', '6', ' ', ' ', '2', ' '], ['#', '28', '#', '3', ' ', ' ', ' ', ' ', '4', ' ', ' ', '20', '#', '29', '7', '28', '22', '26', ' ', ' ', '6', ' ', ' ', '6', ' '], [' ', '25', '18', ' ', ' ', '17', '19', ' ', ' ', '17', '22', '#', '23', '27', ' ', '16', '#', '21', ' ', '17', '26', ' ', '5', '15', '#'], [' ', '6', ' ', ' ', '5', '#', '21', ' ', '5', '30', '23', '27', ' ', '6', ' ', ' ', '25', '31', '7', '30', '18', ' ', ' ', ' ', '#'], [' ', '4', ' ', ' ', ' ', '25', '18', ' ', ' ', ' ', ' ', '6', ' ', '10', '14', '7', '11', ' ', ' ', ' ', ' ', '5', '28', '22', '#'], [' ', ' ', '17', '22', '29', '11', ' ', ' ', '8', '7', '14', '11', ' ', ' ', '6', ' ', ' ', ' ', '2', ' ', ' ', ' ', '20', '#', '#'], [' ', ' ', '16', '23', '18', ' ', '8', '7', '11', ' ', '4', ' ', '1', ' ', '10', '9', ' ', ' ', '4', ' ', '17', '22', '#', '18', ' '], ['#', '19', ' ', ' ', ' ', ' ', '6', ' ', ' ', '1', ' ', ' ', ' ', '1', ' ', '4', ' ', '2', ' ', ' ', '16', '23', '18', ' ', '#'], ['#', '27', ' ', ' ', '17', '22', '#', '3', ' ', ' ', ' ', '8', '3', ' ', '2', ' ', '17', '26', ' ', ' ', ' ', ' ', ' ', '2', ' '], [' ', '10', '28', '29', '30', '23', '27', ' ', '5', '3', ' ', '4', ' ', ' ', '10', '14', '30', '27', ' ', '8', '7', '7', '7', '#', '#'], [' ', ' ', '16', '27', ' ', ' ', '13', '3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '6', ' ', '6', ' ', '6', ' ', ' ', ' ', '4', ' '], ['#', '3', ' ', '4', ' ', '5', '12', ' ', '2', ' ', ' ', '8', '3', ' ', '5', '15', '14', '11', ' ', '4', ' ', '1', ' ', ' ', ' '], ['#', ' ', ' ', ' ', '2', ' ', '6', ' ', '6', ' ', ' ', '4', ' ', '2', ' ', ' ', '6', ' ', '1', ' ', ' ', ' ', '1', ' ', ' '], [' ', '1', ' ', '5', '12', ' ', '24', '29', '15', '14', '3', ' ', '5', '#', '3', ' ', '10', '3', ' ', '17', '22', '19', ' ', ' ', '#'], [' ', ' ', '2', ' ', '6', ' ', '16', '27', ' ', '4', ' ', '1', ' ', '6', ' ', '1', ' ', ' ', '17', '#', '23', '27', ' ', ' ', '#'], [' ', '5', '12', ' ', '6', ' ', ' ', '24', '19', ' ', ' ', ' ', ' ', '4', ' ', ' ', ' ', ' ', '20', '21', ' ', '6', ' ', '2', ' '], ['#', ' ', '4', ' ', '4', ' ', ' ', '20', '#', '22', '29', '3', ' ', ' ', '17', '19', ' ', ' ', '20', '#', '7', '12', ' ', '10', '#'], [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ']]



campaign['win'] = [
list('You Win'+' '*(len('Thanks for playing!')-7)),
list('Game Over'+' '*(len('Thanks for playing!')-9)),
list(' '*len('Thanks for playing!')),
list('Thanks for playing!')
        ]
