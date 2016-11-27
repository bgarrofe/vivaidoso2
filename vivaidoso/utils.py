# -*- coding: latin-1 -*-
faixa_valor_dict = {
    1: 'Gratuito', 
    2: 'Até R$ 1.000', 
    3: 'R$ 1.000 a 3.000',
    4: 'R$ 3.000 a 5.000',
    5: 'R$ 5.000 a 7.000',
    6: 'R$ 7.000 a 10.000',
}

leitos_dict = {
    1: 'Individual',
    2: 'Duplo',
    3: 'Triplo',
    4: 'Quádruplo',
}

dependencia_dict = {
    1: 'Grau 1',
    2: 'Grau 2',
    3: 'Grau 3',
}

sexo_dict = {
    1: 'Masculino',
    2: 'Feminino',
    3: 'Misto',
}

servicos_dict = {
    1: 'Nenhum',
    2: 'Cuidador individual 24hrs',
    3: 'Fisioterapeuta',
    4: 'Terapia Ocupacional',
    5: 'Psicólogo',
    6: 'Acompanhamento médico',
}

def multiple_select_fields(empresa):
    result = {}
    result['faixa_valor'] = ''
    for valor in empresa.faixa_valor:
        result['faixa_valor'] += faixa_valor_dict[int(valor)] + ', '
    result['faixa_valor'] = result['faixa_valor'][:-2]
    
    result['leitos'] = ''
    for valor in empresa.leitos:
        result['leitos'] += leitos_dict[int(valor)] + ', '
    result['leitos'] = result['leitos'][:-2]
    
    result['dependencia'] = dependencia_dict[int(empresa.dependencia)]
    
    result['sexo'] = ''
    for valor in empresa.sexo:
        result['sexo'] += sexo_dict[int(valor)] + ', '
    result['sexo'] = result['sexo'][:-2]
    
    result['servicos'] = ''
    for valor in empresa.servicos_incl:
        result['servicos'] += servicos_dict[int(valor)] + ', '
    result['servicos'] = result['servicos'][:-2]
    
    return result

def upload_path_handler(instance, filename):
    return "images/empresa_{id}/{file}".format(id=instance.empresa.id, file=filename)