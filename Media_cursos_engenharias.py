print('BEM-VINDA AO PROGRAMA QUICK MÉDIA\n')

corretor = input('Digite a plataforma de estimativa do TRI: ')
universidade = input('Digite o nome da universidade na qual você deseja saber sua possível média: ')
curso = input('Digite o curso que deseja: ')

print('\nEscolha o nível da estimativa que você levará em conta:')
print('[1] Notas mínimas')
print('[2] Notas médias')
print('[3] Notas máximas')
nivel = int(input('\nDigite o nível: '))

if nivel == 2:
    str_ling_max = input('\nDigite seu TRI máximo em Linguagens e Códigos de acordo com a plataforma escolhida:')
    str_ling_min = input('Digite seu TRI mínimo em Linguagens e Códigos de acordo com a plataforma escolhida:')
    str_hum_max = input('Digite seu TRI máximo em Ciências Humanas e suas tecnologias de acordo com a plataforma escolhida:')
    str_hum_min = input('Digite seu TRI mínimo em Ciências Humanas e suas tecnologias de acordo com a plataforma escolhida:')
    str_natu_max = input('Digite seu TRI máximo em Ciências da Natureza e suas tecnologias de acordo com a plataforma escolhida:')
    str_natu_min = input('Digite seu TRI mínimo em Ciências da Natureza e suas tecnologias de acordo com a plataforma escolhida:')
    str_mat_max = input('Digite seu TRI máximo em Matemática e suas tecnologias de acordo com a plataforma escolhida:')
    str_mat_min = input('Digite seu TRI mínimo em Matemática e suas tecnologias de acordo com a plataforma escolhida:')
    str_red_med = input('Digite sua possível nota da Redação: ')
  
    ling_max = float(str_ling_max)
    ling_min = float(str_ling_min)
    hum_max = float(str_hum_max)
    hum_min = float(str_hum_min)
    natu_max = float(str_natu_max)
    natu_min = float(str_natu_min)
    mat_max = float(str_mat_max)
    mat_min = float(str_mat_min)
    red_med = float(str_red_med)

    ling_med = (ling_max + ling_min) / 2
    hum_med = (hum_max + hum_min) / 2
    natu_med = (natu_max + natu_min) / 2
    mat_med = (mat_max + mat_min) / 2
    print('\nRELATÓRIO FINAL...')
    print('\nSeu TRI médio foi:')
    print('Ling.:', ling_med)
    print('Hum.:', hum_med)
    print('Natu.:', natu_med)
    print('Mat:', mat_med)

    #Nível 2 
    #emc = Engenharia Mecânica
    peso_ling_ufrj_emc2 = 2*ling_med
    peso_hum_ufrj_emc2 = 1*hum_med
    peso_natu_ufrj_emc2 = 4*natu_med
    peso_mat_ufrj_emc2 = 5*mat_med
    peso_red_ufrj_emc2 = 3*red_med
    multi_ufrj_emc2 = peso_ling_ufrj_emc2 + peso_hum_ufrj_emc2 + peso_natu_ufrj_emc2 + peso_mat_ufrj_emc2 + peso_red_ufrj_emc2
    final_ufrj_emc2 = multi_ufrj_emc2 / 15

    peso_ling_uff_emc2 = 1*ling_med
    peso_hum_uff_emc2 = 1*hum_med
    peso_natu_uff_emc2 = 2*natu_med
    peso_mat_uff_emc2 = 5*mat_med
    peso_red_uff_emc2 = 3*red_med
    multi_uff_emc2 = peso_ling_uff_emc2 + peso_hum_uff_emc2 + peso_natu_uff_emc2 + peso_mat_uff_emc2 + peso_red_uff_emc2
    final_uff_emc2 = multi_uff_emc2 / 12

    peso_ling_cefetrj_emc2 = 1*ling_med
    peso_hum_cefetrj_emc2 = 1*hum_med
    peso_natu_cefetrj_emc2 = 4*natu_med
    peso_mat_cefetrj_emc2 = 4*mat_med
    peso_red_cefetrj_emc2 = 3*red_med
    multi_cefetrj_emc2 = peso_ling_cefetrj_emc2 + peso_hum_cefetrj_emc2 + peso_natu_cefetrj_emc2 + peso_mat_cefetrj_emc2 + peso_red_cefetrj_emc2
    final_cefetrj_emc2 = multi_cefetrj_emc2 / 13

    peso_ling_ufba_emc2 = 2*ling_med
    peso_hum_ufba_emc2 = 2*hum_med
    peso_natu_ufba_emc2 = 4*natu_med
    peso_mat_ufba_emc2 = 5*mat_med
    peso_red_ufba_emc2 = 3*red_med
    multi_ufba_emc2 = peso_ling_ufba_emc2 + peso_hum_ufba_emc2 + peso_natu_ufba_emc2 + peso_mat_ufba_emc2 + peso_red_ufba_emc2
    final_ufba_emc2 = multi_ufba_emc2 / 15

    peso_ling_ufmg_emc2 = 1*ling_med
    peso_hum_ufmg_emc2 = 1*hum_med
    peso_natu_ufmg_emc2 = 1*natu_med
    peso_mat_ufmg_emc2 = 1*mat_med
    peso_red_ufmg_emc2 = 1*red_med
    multi_ufmg_emc2 = peso_ling_ufmg_emc2 + peso_hum_ufmg_emc2 + peso_natu_ufmg_emc2 + peso_mat_ufmg_emc2 + peso_red_ufmg_emc2
    final_ufmg_emc2 = multi_ufmg_emc2 / 5

    peso_ling_cefetmg_emc2 = 1*ling_med
    peso_hum_cefetmg_emc2 = 1*hum_med
    peso_natu_cefetmg_emc2 = 1.5*natu_med
    peso_mat_cefetmg_emc2 = 2.5*mat_med
    peso_red_cefetmg_emc2 = 2*red_med
    multi_cefetmg_emc2 = peso_ling_cefetmg_emc2 + peso_hum_cefetmg_emc2 + peso_natu_cefetmg_emc2 + peso_mat_cefetmg_emc2 + peso_red_cefetmg_emc2
    final_cefetmg_emc2 = multi_cefetmg_emc2 / 8

    peso_ling_utfpr_emc2 = 1*ling_med
    peso_hum_utfpr_emc2 = 1*hum_med
    peso_natu_utfpr_emc2 = 2*natu_med
    peso_mat_utfpr_emc2 = 4*mat_med
    peso_red_utfpr_emc2 = 1*red_med
    multi_utfpr_emc2 = peso_ling_utfpr_emc2 + peso_hum_utfpr_emc2 + peso_natu_utfpr_emc2 + peso_mat_utfpr_emc2 + peso_red_utfpr_emc2
    final_utfpr_emc2 = multi_utfpr_emc2 / 9


    if curso == 'engenharia mecânica':
        print(f'\nCom o TRI estimado pela plataforma {corretor}, cursando Engenharia Mecânica na {universidade}, sua média foi de', end = ' ')

        if universidade == 'ufrj':
            print(f'{final_ufrj_emc2:.2f}')
        
        if universidade == 'uff':
            print(f'{final_uff_emc2:.2f}')
            
        if universidade == 'cefet-rj':
            print(f'{final_cefetrj_emc2:.2f}')

        if universidade == 'ufba':
            print(f'{final_ufba_emc2:.2f}')

        if universidade == 'ufmg':
            print(f'{final_ufmg_emc2:.2f}')

        if universidade == 'cefet-mg':
            print(f'{final_cefetmg_emc2:.2f}')

        if universidade == 'utfpr':
            print(f'{final_utfpr_emc2:.2f}')



    #eca = Engenharia de Controle e Automoção
    peso_ling_ufrj_eca2 = 2*ling_med
    peso_hum_ufrj_eca2 = 1*hum_med
    peso_natu_ufrj_eca2 = 4*natu_med
    peso_mat_ufrj_eca2 = 5*mat_med
    peso_red_ufrj_eca2 = 3*red_med
    multi_ufrj_eca2 = peso_ling_ufrj_eca2 + peso_hum_ufrj_eca2 + peso_natu_ufrj_eca2 + peso_mat_ufrj_eca2 + peso_red_ufrj_eca2
    final_ufrj_eca2 = multi_ufrj_eca2 / 15

    peso_ling_cefetrj_eca2 = 1*ling_med
    peso_hum_cefetrj_eca2 = 1*hum_med
    peso_natu_cefetrj_eca2 = 4*natu_med
    peso_mat_cefetrj_eca2 = 4*mat_med
    peso_red_cefetrj_eca2 = 3*red_med
    multi_cefetrj_eca2 = peso_ling_cefetrj_eca2 + peso_hum_cefetrj_eca2 + peso_natu_cefetrj_eca2 + peso_mat_cefetrj_eca2 + peso_red_cefetrj_eca2
    final_cefetrj_eca2 = multi_cefetrj_eca2 / 13

    peso_ling_ufmg_eca2 = 1*ling_med
    peso_hum_ufmg_eca2 = 1*hum_med
    peso_natu_ufmg_eca2 = 1*natu_med
    peso_mat_ufmg_eca2 = 1*mat_med
    peso_red_ufmg_eca2 = 1*red_med
    multi_ufmg_eca2 = peso_ling_ufmg_eca2 + peso_hum_ufmg_eca2 + peso_natu_ufmg_eca2 + peso_mat_ufmg_eca2 + peso_red_ufmg_eca2
    final_ufmg_eca2 = multi_ufmg_eca2 / 5

    peso_ling_cefetmg_eca2 = 1*ling_med
    peso_hum_cefetmg_eca2 = 1*hum_med
    peso_natu_cefetmg_eca2 = 1.5*natu_med
    peso_mat_cefetmg_eca2 = 2.5*mat_med
    peso_red_cefetmg_eca2 = 2*red_med
    multi_cefetmg_eca2 = peso_ling_cefetmg_eca2 + peso_hum_cefetmg_eca2 + peso_natu_cefetmg_eca2 + peso_mat_cefetmg_eca2 + peso_red_cefetmg_eca2
    final_cefetmg_eca2 = multi_cefetmg_eca2 / 8

    peso_ling_utfpr_eca2 = 1*ling_med
    peso_hum_utfpr_eca2 = 1*hum_med
    peso_natu_utfpr_eca2 = 2*natu_med
    peso_mat_utfpr_eca2 = 4*mat_med
    peso_red_utfpr_eca2 = 1*red_med
    multi_utfpr_eca2 = peso_ling_utfpr_eca2 + peso_hum_utfpr_eca2 + peso_natu_utfpr_eca2 + peso_mat_utfpr_eca2 + peso_red_utfpr_eca2
    final_utfpr_eca2 = multi_utfpr_eca2 / 9

    if curso == 'engenharia de controle e automação':
        print(f'\nCom o TRI estimado pela plataforma {corretor}, cursando Engenharia de Controle e Automação na {universidade}, sua média foi de', end = ' ')

        if universidade == 'ufrj'or 'UFRJ':
            print(f'{final_ufrj_eca2:.2f}')
            
        if universidade == 'cefet-rj' or 'CEFET-RJ':
            print(f'{final_cefetrj_eca2:.2f}')

        if universidade == 'ufmg' or 'UFMG':
            print(f'{final_ufmg_eca2:.2f}')

        if universidade == 'cefet-mg' or 'CEFET-MG':
            print(f'{final_cefetmg_eca2:.2f}')

        if universidade == 'utfpr' or 'UTFPR':
            print(f'{final_utfpr_eca2:.2f}')

    #emt = Engenharia Mecatrônica
    peso_ling_utfpr_emt2 = 1*ling_med
    peso_hum_utfpr_emt2 = 1*hum_med
    peso_natu_utfpr_emt2 = 2*natu_med
    peso_mat_utfpr_emt2 = 4*mat_med
    peso_red_utfpr_emt2 = 1*red_med
    multi_utfpr_emt2 = peso_ling_utfpr_emt2 + peso_hum_utfpr_emt2 + peso_natu_utfpr_emt2 + peso_mat_utfpr_emt2 + peso_red_utfpr_emt2
    final_utfpr_emt2 = multi_utfpr_emt2 / 9

    if curso == 'engenharia mecatrônica':
        print(f'\nCom o TRI estimado pela plataforma {corretor}, cursando Engenharia Mecatrônica na {universidade}, sua média foi de', end = ' ')

        if universidade == 'utfpr' or 'UTFPR':
            print(f'{final_utfpr_emt2:.2f}')

    print('\nNível do TRI:', nivel)
    
if not nivel == 2:
    str_ling = input('\nDigite seu TRI em Linguagens e Códigos de acordo com a plataforma escolhida:')
    str_hum = input('Digite seu TRI em Ciências Humanas e suas tecnologias de acordo com a plataforma escolhida:')
    str_natu = input('Digite seu TRI em Ciências da Natureza e suas tecnologias de acordo com a plataforma escolhida:')
    str_mat = input('Digite seu TRI em Matemática e suas tecnologias de acordo com a plataforma escolhida:')
    str_red = input('Digite sua possível nota da Redação: ')

    ling = float(str_ling)
    hum = float(str_hum)
    natu = float(str_natu)
    mat = float(str_mat)
    red = float(str_red)

    print('\nRELATÓRIO FINAL...')

    #Nível 1 ou 3
    #emc = Engenharia Mecânica
    peso_ling_ufrj_emc = 2*ling
    peso_hum_ufrj_emc = 1*hum
    peso_natu_ufrj_emc = 4*natu
    peso_mat_ufrj_emc = 5*mat
    peso_red_ufrj_emc = 3*red
    multi_ufrj_emc = peso_ling_ufrj_emc + peso_hum_ufrj_emc + peso_natu_ufrj_emc + peso_mat_ufrj_emc + peso_red_ufrj_emc
    final_ufrj_emc = multi_ufrj_emc / 15

    peso_ling_uff_emc = 1*ling
    peso_hum_uff_emc = 1*hum
    peso_natu_uff_emc = 2*natu
    peso_mat_uff_emc = 5*mat
    peso_red_uff_emc = 3*red
    multi_uff_emc = peso_ling_uff_emc + peso_hum_uff_emc + peso_natu_uff_emc + peso_mat_uff_emc + peso_red_uff_emc
    final_uff_emc = multi_uff_emc / 12

    peso_ling_cefetrj_emc = 1*ling
    peso_hum_cefetrj_emc = 1*hum
    peso_natu_cefetrj_emc = 4*natu
    peso_mat_cefetrj_emc = 4*mat
    peso_red_cefetrj_emc = 3*red
    multi_cefetrj_emc = peso_ling_cefetrj_emc + peso_hum_cefetrj_emc + peso_natu_cefetrj_emc + peso_mat_cefetrj_emc + peso_red_cefetrj_emc
    final_cefetrj_emc = multi_cefetrj_emc / 13

    peso_ling_ufba_emc = 2*ling
    peso_hum_ufba_emc = 2*hum
    peso_natu_ufba_emc = 4*natu
    peso_mat_ufba_emc = 5*mat
    peso_red_ufba_emc = 3*red
    multi_ufba_emc = peso_ling_ufba_emc + peso_hum_ufba_emc + peso_natu_ufba_emc + peso_mat_ufba_emc + peso_red_ufba_emc
    final_ufba_emc = multi_ufba_emc / 15

    peso_ling_ufmg_emc = 1*ling
    peso_hum_ufmg_emc = 1*hum
    peso_natu_ufmg_emc = 1*natu
    peso_mat_ufmg_emc = 1*mat
    peso_red_ufmg_emc = 1*red
    multi_ufmg_emc = peso_ling_ufmg_emc + peso_hum_ufmg_emc + peso_natu_ufmg_emc + peso_mat_ufmg_emc + peso_red_ufmg_emc
    final_ufmg_emc = multi_ufmg_emc / 5

    peso_ling_cefetmg_emc = 1*ling
    peso_hum_cefetmg_emc = 1*hum
    peso_natu_cefetmg_emc = 1.5*natu
    peso_mat_cefetmg_emc = 2.5*mat
    peso_red_cefetmg_emc = 2*red
    multi_cefetmg_emc = peso_ling_cefetmg_emc + peso_hum_cefetmg_emc + peso_natu_cefetmg_emc + peso_mat_cefetmg_emc + peso_red_cefetmg_emc
    final_cefetmg_emc = multi_cefetmg_emc / 8

    peso_ling_utfpr_emc = 1*ling
    peso_hum_utfpr_emc = 1*hum
    peso_natu_utfpr_emc = 2*natu
    peso_mat_utfpr_emc = 4*mat
    peso_red_utfpr_emc = 1*red
    multi_utfpr_emc = peso_ling_utfpr_emc + peso_hum_utfpr_emc + peso_natu_utfpr_emc + peso_mat_utfpr_emc + peso_red_utfpr_emc
    final_utfpr_emc = multi_utfpr_emc / 9

    if curso == 'engenharia mecânica':
        print(f'\nCom o TRI estimado pela plataforma {corretor}, cursando Engenharia Mecânica na {universidade}, sua média foi de', end = ' ')

        if universidade == 'ufrj' or 'UFRJ':
            print(f'{final_ufrj_emc:.2f}')
        
        if universidade == 'uff' or 'UFF':
            print(f'{final_uff_emc:.2f}')
            
        if universidade == 'cefet-rj' or 'CEFET-RJ':
            print(f'{final_cefetrj_emc:.2f}')

        if universidade == 'ufba' or 'UFBA':
            print(f'{final_ufba_emc:.2f}')

        if universidade == 'ufmg' or 'UFMG':
            print(f'{final_ufmg_emc:.2f}')

        if universidade == 'cefet-mg' or 'CEFET-MG':
            print(f'{final_cefetmg_emc:.2f}')

        if universidade == 'utfpr' or 'UTFPR':
            print(f'{final_utfpr_emc:.2f}')

    #eca = Engenharia de Controle e Automoção
    peso_ling_ufrj_eca = 2*ling
    peso_hum_ufrj_eca = 1*hum
    peso_natu_ufrj_eca = 4*natu
    peso_mat_ufrj_eca = 5*mat
    peso_red_ufrj_eca = 3*red
    multi_ufrj_eca = peso_ling_ufrj_eca + peso_hum_ufrj_eca + peso_natu_ufrj_eca + peso_mat_ufrj_eca + peso_red_ufrj_eca
    final_ufrj_eca = multi_ufrj_eca / 15

    peso_ling_cefetrj_eca = 1*ling
    peso_hum_cefetrj_eca = 1*hum
    peso_natu_cefetrj_eca = 4*natu
    peso_mat_cefetrj_eca = 4*mat
    peso_red_cefetrj_eca = 3*red
    multi_cefetrj_eca = peso_ling_cefetrj_eca + peso_hum_cefetrj_eca + peso_natu_cefetrj_eca + peso_mat_cefetrj_eca + peso_red_cefetrj_eca
    final_cefetrj_eca = multi_cefetrj_eca / 13

    peso_ling_ufmg_eca = 1*ling
    peso_hum_ufmg_eca = 1*hum
    peso_natu_ufmg_eca = 1*natu
    peso_mat_ufmg_eca = 1*mat
    peso_red_ufmg_eca = 1*red
    multi_ufmg_eca = peso_ling_ufmg_eca + peso_hum_ufmg_eca + peso_natu_ufmg_eca + peso_mat_ufmg_eca + peso_red_ufmg_eca
    final_ufmg_eca = multi_ufmg_eca / 5

    peso_ling_cefetmg_eca = 1*ling
    peso_hum_cefetmg_eca = 1*hum
    peso_natu_cefetmg_eca = 1.5*natu
    peso_mat_cefetmg_eca = 2.5*mat
    peso_red_cefetmg_eca = 2*red
    multi_cefetmg_eca = peso_ling_cefetmg_eca + peso_hum_cefetmg_eca + peso_natu_cefetmg_eca + peso_mat_cefetmg_eca + peso_red_cefetmg_eca
    final_cefetmg_eca = multi_cefetmg_eca / 8

    peso_ling_utfpr_eca = 1*ling
    peso_hum_utfpr_eca = 1*hum
    peso_natu_utfpr_eca = 2*natu
    peso_mat_utfpr_eca = 4*mat
    peso_red_utfpr_eca = 1*red
    multi_utfpr_eca = peso_ling_utfpr_eca + peso_hum_utfpr_eca + peso_natu_utfpr_eca + peso_mat_utfpr_eca + peso_red_utfpr_eca
    final_utfpr_eca = multi_utfpr_eca / 9

    if curso == 'engenharia de controle e automação':
        print(f'\nCom o TRI estimado pela plataforma {corretor}, cursando Engenharia de Controle e Automação na {universidade}, sua média foi de', end = ' ')

        if universidade == 'ufrj' or 'UFRJ':
            print(f'{final_ufrj_eca:.2f}')
            
        if universidade == 'cefet-rj' or 'CEFET-RJ':
            print(f'{final_cefetrj_eca:.2f}')

        if universidade == 'ufmg' or 'UFMG':
            print(f'{final_ufmg_eca:.2f}')

        if universidade == 'cefet-mg' or 'CEFET-MG':
            print(f'{final_cefetmg_eca:.2f}')

        if universidade == 'utfpr' or 'UTFPR':
            print(f'{final_utfpr_eca:.2f}')


    #emt = Engenharia Mecatrônica
    peso_ling_utfpr_emt = 1*ling
    peso_hum_utfpr_emt = 1*hum
    peso_natu_utfpr_emt = 2*natu
    peso_mat_utfpr_emt = 4*mat
    peso_red_utfpr_emt = 1*red
    multi_utfpr_emt = peso_ling_utfpr_emt + peso_hum_utfpr_emt + peso_natu_utfpr_emt + peso_mat_utfpr_emt + peso_red_utfpr_emt
    final_utfpr_emt = multi_utfpr_emt / 9

    if curso == 'engenharia mecatrônica':
        print(f'\nCom o TRI estimado pela plataforma {corretor}, cursando Engenharia Mecatrônica na {universidade}, sua média foi de', end = ' ')

        if universidade == 'utfpr' or 'UTFPR':
            print(f'{final_utfpr_emt:.2f}')

    print('\nNível do TRI:', nivel)
