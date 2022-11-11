from django.shortcuts import render

from djangoProject.forms import UserForm


def calcularFaixaImc(imc, sexo, peso, altura):
    if peso <= 0 and altura <= 0:
        return "O Peso e a Altura não podem ser menor ou igual a zero"
    if peso <= 0:
        return "Peso nao pode ser menor ou igual a zero"
    if altura <= 0:
        return "Altura nao pode ser menor ou igual a zero"
    else:
        if sexo == "F":
            if imc < 19.1:
                return "abaixo do peso";
            else:
                if imc < 25.8:
                    return "no peso normal";
                else:
                    if imc < 27.3:
                        return "marginalmente acima do peso";
                    else:
                        if imc < 32.3:
                            return "acima do peso ideal";
                        else:
                            return "obesa";
        if sexo == "M":
            if imc < 20.7:
                return "abaixo do peso";
            else:
                if imc < 26.4:
                    return "no peso normal";
                else:
                    if imc < 27.8:
                        return "marginalmente acima do peso";
                    else:
                        if imc < 31.1:
                            return "acima do peso ideal";
                        else:
                            return "obeso";
        else:
            return "Sexo Inexistente"


def home(request):
    global estado_atual, imc_real
    if request.method == "GET":
        formulario = UserForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'index.html', context=context)
    else:
        formulario = UserForm(request.POST)
        if formulario.is_valid():
            peso = request.POST.get('peso')
            altura = request.POST.get('altura')
            sexo = request.POST.get('sexo')
            imc = 0
            if float(peso) > 0 and float(altura) > 0:
                imc = float(peso) / (float(altura) * float(altura))

            imc_real = round(imc, 1)
            estado_atual = calcularFaixaImc(imc_real, sexo, float(peso), float(altura))


        context = {
            'formulario': formulario,
            'imc': imc_real,
            'estadoAtual': estado_atual
        }

        return render(request, 'index.html', context=context)
