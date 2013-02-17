from time import sleep
import sys
from Daemon import Daemon
import functions
summary = 'Wifi watcher'

# A simple daemon that makes my life a little bit easier
# Alfonso Perez

class WifiWatcherDaemon(Daemon):
    
    def run(self):

        wait_time = 1
    
        userlist = list()
        userlist.extend(functions.getUsers(functions.getHtml()))
        
        print ('Daemon started.\n')
        functions.notification(summary, 'The daemon has started. Now watching for new users in the wlan...')
        print('The users in the WLAN right now are:')
    
        for u in userlist:
            print (str(u[0]) + ' ' + str(u[1]))
        
        print ('\n')
        
        while(True):     
            
            users = functions.getUsers(functions.getHtml())
        
            for u in users:
    
                if u not in userlist:  
                    note = functions.print_user(u) + ' has connected to the wlan' 
                    print (note)
                    functions.notification(summary, note)
                    userlist.append(u)      
                    
            if len(users) < len(userlist): 
                for u in userlist:
                    if u not in users:
                        note = functions.print_user(u) + ' has disconnected from the wlan'
                        print (note)
                        functions.notification(summary, note)
                        userlist.remove(u)
                                                   
        sleep(wait_time)
        
  
def main():

    daemon = WifiWatcherDaemon('/tmp/wifiwatcher-daemon.pid')

    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print ("Unknown command")
            sys.exit(2)
            sys.exit(0)
    else:
        print ("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)


main()    