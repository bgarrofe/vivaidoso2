# -*- coding: latin-1 -*-
from django.db.models import Q

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

def search_filter(request):
    
    tipo = request.POST.get('tipo')
    q_final = Q(tipo=tipo)

    dependencia = request.POST.get('dependencia')
    q_final.add(Q(dependencia=dependencia), Q.AND)
    
    q_objects = Q()
    bairro = request.POST.getlist('bairro')
    for item in bairro:
        q_objects.add(Q(bairro=item), Q.OR)
    q_final.add(q_objects, Q.AND)
    
    q_objects = Q()
    faixa_valor = request.POST.getlist('faixa_valor')
    for item in faixa_valor:
        q_objects.add(Q(faixa_valor__contains=item), Q.OR)
    q_final.add(q_objects, Q.AND)

    q_objects = Q()
    leitos = request.POST.getlist('leitos')
    for item in leitos:
        q_objects.add(Q(leitos__contains=item), Q.OR)
    q_final.add(q_objects, Q.AND)

    q_objects = Q()
    sexo = request.POST.getlist('sexo')
    for item in sexo:
        q_objects.add(Q(sexo__contains=item), Q.OR)
    q_final.add(q_objects, Q.AND)
    
    q_objects = Q()
    servicos_incl = request.POST.getlist('servicos_incl')
    for item in servicos_incl:
        q_objects.add(Q(servicos_incl__contains=item), Q.OR)
    q_final.add(q_objects, Q.AND)
    
    return q_final

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