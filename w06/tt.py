import optparse
import time
parse = optparse.OptionParser()
parse.add_option("-w", "--maxwidth", dest="max_sirka", type="int", help="max_sirka_hodnota, default  %default")
parse.set_defaults(max_sirka=100)
opts, args = parse.parse_args()
while True:
    print("maxwidth: {:d}".format(opts.max_sirka))
    time.sleep(1)