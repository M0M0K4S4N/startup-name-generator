from src import namer
import json

# cli command to run the namer function
def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('seed', type=str, help='seed names')
    parser.add_argument('-p', '--paginate', action='store_true', help='make things a bit easier to read')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    args = parser.parse_args()
    word_list = namer(args.seed)
    
    # paginate  
    if args.paginate:
        word_list = [word_list[i:i + 9] for i in range(0, len(word_list), 9)]
    print(json.dumps(word_list, indent=2))
    
if __name__ == '__main__':
    main()
