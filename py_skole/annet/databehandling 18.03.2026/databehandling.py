import csv
import matplotlib.pyplot as plt

with open('05576_laererutdanninger_og_pedagogikk_bearbeidet.csv', encoding='utf-8') as f:
    file = csv.reader(f, delimiter=';')

    #oppgave a
    f.seek(0)
    next(file)
    xvalues = [int(i[0]) for i in file]
    f.seek(0)
    next(file)
    ymenn = [int(i[1]) for i in file]
    f.seek(0)
    next(file)
    ykvinner = [int(i[2]) for i in file]

    plt.plot(xvalues, ymenn, label='menn')
    plt.plot(xvalues, ykvinner, label='kvinner')
    plt.xlabel('år')
    plt.ylabel('studenter')
    plt.legend()
    plt.show()
    
    #oppgave b
    f.seek(0)
    next(file)
    totaler = [int(i[1]) + int(i[2]) for index, i in enumerate(file)]
    minstetotal = min(totaler)
    minsteår = totaler.index(minstetotal)
    print(f'minst: året {xvalues[minsteår]}, var det totalt {minstetotal}')
    

    #oppgave c
    mestetotal = max(totaler)
    mesteår = totaler.index(mestetotal)
    print(f'mest: året {xvalues[mesteår]}, var det totalt {mestetotal}')

    #oppgave d
    heleperioden = sum(ymenn) + sum(ykvinner)
    print(f'andel heleperioden: andelen kvinner var {round((sum(ykvinner)/heleperioden)*100)}%, andelen menn var {round((sum(ymenn)/heleperioden)*100)}%')
    
    #oppgave e
    femår = sum(ymenn[0:5]) + sum(ykvinner[0:5])
    print(f'andel 5 første år: andelen kvinner var {round((sum(ykvinner[0:5])/femår)*100)}%, andelen menn var {round((sum(ymenn[0:5])/femår)*100)}%')

    #oppgave f
    ymenn.reverse()
    ykvinner.reverse()
    sistefemår = sum(ymenn[0:5]) + sum(ykvinner[0:5])
    print(f'andel 5 siste år: andelen kvinner var {round((sum(ykvinner[0:5])/sistefemår)*100)}%, andelen menn var {round((sum(ymenn[0:5])/sistefemår)*100)}%')

    #oppgave g
    '''
    På grafen kan vi se at det har vært langt flere kvinner enn menn, alle årene, og at det har økt antall for begge utover årene.
    Vi ser også at det var mest studenter i 2021, som betyr at studiet har blitt mer populært generelt utover årene. (Året det var minst var 2006).
    De siste fem årene har andelen menn blitt litt større enn de første fem årene, men økningen er svært liten med 5%
    
    '''
    
