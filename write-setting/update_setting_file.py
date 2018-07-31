import configparser, os, time

iniFilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini')

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config['setting'] = {'mode': 'mode' + str(time.time())}
    with open(iniFilePath, 'w') as configfile:
        config.write(configfile)

