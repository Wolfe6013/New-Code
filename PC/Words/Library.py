import time

def Library():
    Leave = 0
    while Leave == 0:
        time.sleep(0.9)
        LBSaB1 = ["Shadow and Bone","Leigh Bardugo"]
        LBSaB2 = ["Siege and Storm","Leigh Bardugo"]
        LBSaB3 = ["Ruin and Rising","Leigh Bardugo"]
        LBSoC1 = ["Six of Crows","Leigh Bardugo"]
        LBSoC2 = ["Crooked Kingdom","Leigh Bardugo"]
        LBKoS1 = ["King of Scars","Leigh Bardugo"]
        LBKoS2 = ["Rule of Wolves","Leigh Bardugo"]
        MMR1 = ["Renegades","Marissa Meyer"]
        MMR2 = ["Archenemies","Marissa Meyer"]
        MMR3 = ["Supernova","Marissa Meyer"]
        PNtKoNLG1 = ["The Knife of Never Letting Go","Patrick Ness"]
        PNtKoNLG2 = ["The Ask and the Answer","Patrick Ness"]
        PNtKoNLG3 = ["Monsters of Men","Patrick Ness"]
        TMS0 = ["The Outcast","Taran Matharu"]
        TMS1 = ["The Novice","Taran Matharu"]
        TMS2 = ["The Inquisition","Taran Matharu"]
        TMS3 = ["The Battlemage","Taran Matharu"]
        CPE1 = ["Eragon","Christopher Paolini"]
        CPE2 = ["Eldest","Christopher Paolini"]
        CPE3 = ["Brisingr","Christopher Paolini"]
        CPE4 = ["Inheritance","Christopher Paolini"]
        JTNtToMC1 = ["Nevermoor: The Trials of Morrigan Crow","Jessica Townsend"]
        JTNtToMC2 = ["Hollowpox: The Hunt for Morrigan Crow","Jessica Townsend"]
        JTNtToMC3 = ["Wundersmith: The Calling of Morrigan Crow","Jessica Townsend"]
        JTNtToMC4 = ["Silverborn: The Mystery of Morrigan - Unreleased","Jessica Townsend"]
        GNS0 = ["Clariel","Garth Nix"]
        GNS1 = ["Sabriel","Garth Nix"]
        GNS2 = ["Lirael","Garth Nix"]
        GNS3 = ["Abhorsen","Garth Nix"]
        GNS4 = ["The Creature in the Case","Garth Nix"]
        GNS5 = ["Goldenhand","Garth Nix"]
        GNtLHBoL1 = ["The Left-Handed Booksellers of London","Garth Nix"]
        GNtLHBoL2 = ["The Sinister Booksellers of Bath","Garth Nix"]
        JDtMR1 = ["The Maze Runner","James Dashner"]
        JDtMR2 = ["The Scorch Trials","James Dashner"]
        JDtMR3 = ["The Death Cure","James Dashner"]
        PRME1 = ["Mortal Engines","Philip Reeve"]
        PRME2 = ["Predator's Gold","Philip Reeve"]
        PRME3 = ["Infernal Devices","Philip Reeve"]
        PRME4 = ["A Darkling Plain","Philip Reeve"]
        library = [LBSaB1,LBSaB2,LBSaB3,LBSoC1,LBSoC2,LBKoS1,LBKoS2,MMR1,MMR2,MMR3,PNtKoNLG1,PNtKoNLG2,PNtKoNLG3,TMS0,TMS1,TMS2,TMS3,CPE1,CPE2,CPE3,CPE4,JTNtToMC1,JTNtToMC2,JTNtToMC3,JTNtToMC4,GNS0,GNS1,GNS2,GNS3,GNS4,GNS5,GNtLHBoL1,GNtLHBoL2,JDtMR1,JDtMR2,JDtMR3,PRME1,PRME2,PRME3,PRME4]
        codelist = ['LBSaB1','LBSaB2','LBSaB3','LBSoC1','LBSoC2','LBKoS1','LBKoS2','MMR1','MMR2','MMR3','PNtKoNLG1','PNtKoNLG2','PNtKoNLG3','TMS0','TMS1','TMS2','TMS3','CPE1','CPE2','CPE3','CPE4','JTNtToMC1','JTNtToMC2','JTNtToMC3','JTNtToMC4','GNS0','GNS1','GNS2','GNS3','GNS4','GNS5','GNtLHBoL1','GNtLHBoL2','JDtMR1','JDtMR2','JDtMR3','PRME1','PRME2','PRME3','PRME4']
        SearchType = input('Browse, Author, Book Name, Code or Leave? ')
        if SearchType == 'Count':     ###admin, to see how many books are in the library and the codelist
            for LibraryDone, x in enumerate(library):
                ...     ###to calculate how many books it should be, do {EndOfLibraryLine}-{StartOfLibraryLine}+1
            print(f'There is {LibraryDone+1} books in library')
            for CodeDone, x in enumerate(library):
                ...     ###should match LibraryDone
            print(f'There is {CodeDone+1} books in code list')
        if SearchType == 'Leave':     ###stops the 'while' loop
            Leave = 1
        if SearchType == 'Browse':     ###prints the full library (do not do if library too big)
            for BrowseDone, x in enumerate(codelist):
                print(f'{BrowseDone+1} - {x} -', end=' ')
                BookNumber = library[codelist.index(x)]
                print(f'{BookNumber[0]} by', end=' ')
                print(f'{BookNumber[1]}')
                time.sleep(0.1)
        if SearchType == 'Browse Slow':     ###same as browse, only slower, so you can read easier
            for SlowTimeDone, x in enumerate(library):
                ...
            print(f'It will take {(SlowTimeDone+1)/2} seconds')
            confirm = input('Do you want to procceed? (Y/N) ')
            if confirm == 'Y':
                for BrowseSlowDone, x in enumerate(codelist):
                    print(f'{BrowseSlowDone+1} - {x} -', end=' ')
                    BookNumber = library[codelist.index(x)]
                    print(f'{BookNumber[0]} by', end=' ')
                    print(f'{BookNumber[1]}')
                    time.sleep(0.5)
        if SearchType == 'Author':     ###prints every book that author has written that we have in the library
            BookFound = 0
            AuthorName = input('What do you want to search for? ')
            for x in library:
                if AuthorName in x[1]:
                    BookNumber = library.index(x)
                    print(f'{codelist[BookNumber]} -', end=' ')
                    print(f'{x[0]} by', end=' ')
                    print(f'{x[1]}')
                    BookFound = 1
                    time.sleep(0.1)
            if BookFound == 0:
                print(f'Nothing found with that author')
        if SearchType == 'Book Name':     ###prints the book you search for (if we have it)
            BookFound = 0
            AuthorName = input('What do you want to search for? ')
            for x in library:
                if AuthorName in x[0]:
                    BookNumber = library.index(x)
                    print(f'{codelist[BookNumber]} -', end=' ')
                    print(f'{x[0]} by', end=' ')
                    print(f'{x[1]}')
                    BookFound = 1
                    time.sleep(0.1)
            if BookFound == 0:
                print(f'No books found with that name')
        if SearchType == 'Code':     ###prints every book containing the code you put in
            BookFound = 0
            LibraryCode = input('What is the books code? ')
            for x in codelist:
                if LibraryCode in x:
                    print(f'{x} -', end=' ')
                    BookNumber = codelist.index(x)
                    print(f'{library[BookNumber]}')
                    BookFound = 1
                    time.sleep(0.1)
            if BookFound == 0:
                print(f'No books found with that code')
Library()