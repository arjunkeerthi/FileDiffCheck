import sys;

def main():
    args = sys.argv[1:];
    
    noStrip = False;
    if args[0] == '-nostrip' or args[0] == '-ns' :
        noStrip = True;
        del args[0];
    
    writeFile = False;
    if args[0] == '-file' or args[0] == '-f' :
        writeFile = True;
        del args[0];
        
    file1 = open(args[0],'r');
    file2 = open(args[1],'r');
    
    f1 = file1.read();
    f2 = file2.read();
    if noStrip:
        f1 = f1.split('\n');
        f2 = f2.split('\n');
    else :
        f1 = f1.strip().split('\n');
        f2 = f2.strip().split('\n');
        
    if len(args) < 2 or len(args) > 3 :
        print('Error with provided command-line arguments. Usage: [-nostrip] [-file] file1 file2 [output file]');
        sys.exit(1);
    elif len(args) == 2 and writeFile :
        print('Output file name not provided. Usage: [-nostrip] [-file] file1 file2 [output file]');
        sys.exit(1);
    elif len(args) == 3 and not writeFile :
        print('Argument provided for output file without tag (\'-file\' or \'-f\'). Usage: [-nostrip] [-file] file1 file2 [output file]');
        sys.exit(1);
    
    fout = None;
    if writeFile :
        fout = open(args[2],'w');
        fout.write('File 1: ' + args[0] + '\n');
        fout.write('File 2: ' + args[1] + '\n');
        fout.write('\nDifferences are displayed below, along with the corresponding line number.\n');
    else :
        print('File 1: ' + args[0]);
        print('File 2: ' + args[1]);
        print('\nDifferences are displayed below, along with the corresponding line number.');

    if len(f1) != len(f2) :
        if writeFile:
            fout.write('Note: Number of lines in each file is different. Will only compare up through shorter file.\n');
        else :
            print('Note: Number of lines in each file is different. Will only compare up through shorter file.');
    
    if writeFile :
        fout.write('\n');
    else : 
        print();
    
    diffCount = 0;
    for i in range(min(len(f1),len(f2))) :
        if f1[i] != f2[i]:
            diffCount += 1;
            if writeFile :
                fout.write('Line ' + str(i+1) + ': \n    File 1: ' + f1[i] + '\n    File 2: ' + f2[i] + '\n\n');
            else :
                print('Line ' + str(i+1) + ': \n    File 1: ' + f1[i] + '\n    File 2: ' + f2[i] + '\n');
    if diffCount == 0 : 
        if writeFile :
            fout.write('No differences detected.');
        else :
            print('No differences detected.');
                
    if writeFile : print('File comparison data has been written to ' + args[2]);
                
    file1.close();
    file2.close();
    
if __name__ == '__main__':
    main();