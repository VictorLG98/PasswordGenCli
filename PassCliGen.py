import argparse
import os
import pathlib
from PassGen import gen_pass

parser = argparse.ArgumentParser(description="Programa que genera contraseñas seguras.",
                                 prog="Password Cli Generator", epilog='Created by @_Vic_Vic_98')

parser.add_argument('-l', '--longitud', type=int, help='Longitud de la contraseña.')
parser.add_argument('-v', '--version', action='store_true', default=False, help='Muestra la versión.')
parser.add_argument('-s', '--save', help='Creará un archivo para almacenar la contraseña.')

args = parser.parse_args()

if __name__ == '__main__':
    if args.version:
        os.system('echo 1.0')

    if args.longitud and args.save:
        password = gen_pass(args.longitud)
        os.system(f'echo La contraseña es: {password}')
        os.system(f'echo {password} > {args.save}')
        os.system(f'echo La contraseña se ha guardado en: {pathlib.Path().absolute()}/{args.save}')
    elif args.longitud:
        password = gen_pass(args.longitud)
        os.system(f'echo La contraseña es: {password}')
