import idautils
import idc
import idaapi
import getpass

print("""
        
  _     _       _____                              _      ______                _   _             __  __             ______                          _           _     _ 
 (_)   | |     |  __ \                            (_)    |  ____|              | | (_)           |  \/  |           |  ____|         /\             | |         (_)   | |
  _  __| | __ _| |  | |_   _ _ __   __ _ _ __ ___  _  ___| |__ _   _ _ __   ___| |_ _  ___  _ __ | \  / | __ _ _ __ | |__ ___  _ __ /  \   _ __   __| |_ __ ___  _  __| |
 | |/ _` |/ _` | |  | | | | | '_ \ / _` | '_ ` _ \| |/ __|  __| | | | '_ \ / __| __| |/ _ \| '_ \| |\/| |/ _` | '_ \|  __/ _ \| '__/ /\ \ | '_ \ / _` | '__/ _ \| |/ _` |
 | | (_| | (_| | |__| | |_| | | | | (_| | | | | | | | (__| |  | |_| | | | | (__| |_| | (_) | | | | |  | | (_| | |_) | | | (_) | | / ____ \| | | | (_| | | | (_) | | (_| |
 |_|\__,_|\__,_|_____/ \__, |_| |_|\__,_|_| |_| |_|_|\___|_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|_|  |_|\__,_| .__/|_|  \___/|_|/_/    \_\_| |_|\__,_|_|  \___/|_|\__,_|
                        __/ |                                                                                 | |                                                        
                       |___/                                                                                  |_|                                                        
                       
                                             
  ---------------------------------------------------
  | Twitter: https://twitter.com/zayotem            |
  | Github: https://github.com/ZAYOTEM              |
  | Authors:Halil FILIK, Hakan SOYSAL               |
  ---------------------------------------------------                      
                       
                            """)


username=getpass.getuser()

condition = """
auto fp;
auto ea;
auto y;
fp = fopen(\"C:\\\\Users\\\\"""+username+"""\\\\Desktop\\\\dfm_output.txt\", \"a\");
ea = GetEventEa();
y = GetFunctionName(ea);
fprintf(fp,\"%s\\n\",y);
DelBpt(ea);
fclose(fp);
""" 

for function_ea in idautils.Functions():
    idc.add_bpt(function_ea, 1, BPT_EXEC)
    idc.set_bpt_cond(function_ea, condition)

    
print("""
  ______     __     ______ _______ ______ __  __ 
 |___  /   /\\ \   / / __ \__   __|  ____|  \/  |
    / /   /  \\ \_/ / |  | | | |  | |__  | \  / |
   / /   / /\ \\   /| |  | | | |  |  __| | |\/| |
  / /__ / ____ \| | | |__| | | |  | |____| |  | |
 /_____/_/    \_\_|  \____/  |_|  |______|_|  |_|
                                                 
                                                 
""")    