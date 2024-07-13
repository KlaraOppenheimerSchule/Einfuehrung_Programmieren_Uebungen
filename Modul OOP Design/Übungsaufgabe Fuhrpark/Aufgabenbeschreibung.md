# Aufgabe Fuhrpark

## Schwierigkeitsgrad: * * * * *

## Text der Aufgabe
Sie sollen für ein Autofahrsimulationsprogramm einen passenden Fuhrpark in objektorientierter Form entwerfen. Folgende Fahrzeugklassen soll es geben:
 
•	Firebird: Es handelt sich hierbei um einen Firebird. Beim Firebird ist wie bei allen anderen Autos auch der Hersteller gespeichert. Eine Besonderheit ist beim Firebird, das darüberhinaus auch die Wattzahl der Unterbodenbelichtung bekannt ist. Der Firebird gibt beim Aufruf der Methode fahren „Brummbrumm“  aus. Der Firebird ist der Kategorie Rennwagen zugeordnet.

•	Weitere Rennwagen: Ferner existieren zwei weitere Rennwagen in Ihrem Fuhrpark. Im Rahmen von ausgiebigen Testphasen zeigte sich, dass das obere Auto, ein Model Majorette Turbo, beim Aufruf der Methode fahren, nicht „Brummbrumm“ macht sondern „Uuhweemmn“.  Zudem ist beim Majorette Turbo die jeweilige Anzahl der Flügeltüren gespeichert. Das rechte Auto, vom Typ Fire Turbo, gibt ebenfalls wie der Firebird „Brummbrumm“ aus. Zudem ist gespeichert, ob der Turbo beim Fire Turbo angeschalten ist. 

•	Freizeitwagen: Der Fuhrpark verfügt weiterhin über einen Mercedes Benz vom Typ AMG. Dieses Auto entspricht nicht der Kategorie Rennwagen, sondern der Kategorie Freizeitwagen. Die Freizeitwagen zeichnen sich unter anderen dadurch aus, dass diese zum Teil über eine integrierte Minibar verfügen. Ob dies der Fall ist, ist in der entsprechenden Klasse vermerkt. Beim Mercedes Benz Typ AMG ist zudem vermerkt, ob eine Wegfahrsperre vorhanden ist. Alle Freizeitwagen geben beim Aufruf ihrer Methode fahren ein „scheeechuiehh“ aus.

•	Beachcar: Ein weiterer Freizeitwagen ist ein Beachcar. Was dieses Auto besonders macht ist die Fähigkeit, auch Sprünge vollführen zu können -  in der Ausgabe erscheint beim Aufruf dieser Methode JumpJump. Ferner verfügt das Auto in vielen Fällen über einen ausklappbaren Sonnenschutz.

•	Lowrider: Da die Sprungfunktionalität bei unseren Kunden besonders gut ankommt, soll es zudem vom Firebird eine Spezialisieurng geben, die die Sprungfähigkeit inne hat. Dort jedoch nicht in Form der Ausgabe von „JumpJump“ , sondern durch die Ausgabe von „I am a Lowrider“. Der Auftraggeber möchte dabei sichergestellt haben, dass alle Autos, die eine Sprungfunktionalität versprechen, diese auch tatsächlich ausführen können. 

•	Fuhrparkverwalter: Es soll zudem eine Klasse Fuhrparkverwalter geben, die über eine typsichere Collection verfügt, mittels derer auf alle vorhandenen Instanzen des Fuhrparks zugegriffen werden kann. Der Fuhrparkverwalter soll zudem, nach einem Aufruf seiner Methode checkFuhrpark, alle Autos Probe fahren lassen. Der Fuhrparkverwalter ist es auch, der jedem Auto bei der Erstellung eine AutoID zuweist, die jedes Auto im Fuhrpark eindeutig identifizierbar macht. 


Erstellen Sie ein passendes Klassendiagramm und sprechen Sie dieses mit Ihrer Lehrkraft ab, bevor Sie es dieses implementieren.

## Optionale Erweiterung
•	Ein einzigartiger Fuhrparkverwalter: Der Kunde fordert nun im Rahmen der Programmgestaltung, dass zu jedem Zeitpunkt immer nur eine Instanz der Klasse Fuhrparkverwalter geben darf. Ein Kollege hat darauf hin von einer möglichen Umsetzung im Rahmen des sogenannten Singleton-Patterns gesprochen. Finden Sie hierzu passende Informationen im Internet .

•	Ein Kollege meint, wenn der Fuhrparkverwalter eine generische Liste des Typs Auto hält, würde damit eine dynamische Polymorphie ermöglicht. Versuchen Sie zu klären, was damit gemeint ist.

•	Der Fuhrparkverwalter will springen: Ihr Fuhrparkverwalter möcht nun alle Autos seines Fuhrparks springen lassen, sofern die jeweilige Autos über eine passende Sprungfunktion verfügen. Erstellen Sie zu diesem Zweck eine Methode der Klasse Fuhrparkverwalter, die diesem Wunsch gerecht wird. Rufen Sie anschließen