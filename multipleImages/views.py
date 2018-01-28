from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.shortcuts import redirect


# Create your views here.

def index(request):
        if request.method == 'POST':
            try:
                fname = request.POST['fname']
                phone = request.POST['phone']
                recipeName = request.POST['recipeName']
                ingredients = request.POST['ingredients']
                method = request.POST['method']
                useremail = request.POST['email']
                url = request.POST['url']
                plaintexts = get_template('email.txt')
                htmlys = get_template('addRecipeTemplate.html')
                user_context = {'fname': fname}
                text_content = plaintexts.render(user_context)
                html_contents = htmlys.render(user_context)
                email = EmailMultiAlternatives('Thank you for getting in touch!', text_content, to=[useremail])
                email.attach_alternative(html_contents, "text/html")
                try:
                    email.send()
                    try:
                        plaintext = get_template('email.txt')
                        htmly = get_template('addRecipesAdmintemplates.html')
                        admin_context = {'url': url, 'fname': fname, 'email': useremail, 'phone': phone,
                                         'recipeName': recipeName, 'ingredients': ingredients, 'method': method}

                        text_contents = plaintext.render(admin_context)

                        html_content = htmly.render(admin_context)

                        template = get_template('addRecipesAdmintemplates.html')

                        content = template.render(admin_context)

                        email = EmailMessage('Query For Add Recipes', content, to=['xxxxx@gmail.com'])

                        for f in request.FILES.getlist('recipeImage'):
                            email.attach(f.name, f.read(), f.content_type)

                        email.send()
                        return render(request, "thankyou.html")

                    except Exception as e:
                        import ipdb; ipdb.set_trace()
                        return render(request, "thankyou.html")

                except Exception as e:
                    import ipdb; ipdb.set_trace()
                    return redirect('/')

            except Exception as e:
                import ipdb; ipdb.set_trace()

                return render(request, "base.html")

        else:
            return render(request, "base.html")

