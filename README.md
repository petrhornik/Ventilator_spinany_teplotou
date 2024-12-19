# VENTILÁTOR SPÍNANÝ TEPLOTOU

## CÍL:

Cílem tohoto projektu je vytvořit automatický chladící systém pro fotovoltaickou elektrárnu, z důvodu jejího neustálého přehřívání při vysokém využijí v letních sezónách. Projekt jsem se rozhodl vytvořit, jelikož mi přišlo zbytečné nechávat neustále puštěný ventilátor, který zbytečně spotřebovává energii i během noci když není potřeba. 

## Použité komponenty

- Raspberry Pi pico 2 WH
- Grove Shield pro RPi Pico v1.0
- Grove - Relé
- Vodotěsný teplotní senzor DS18B20
- 1x Adaptér Grove na pin
- 2x Grove 4pinový propojovací kabel žena-žena - 10 cm

Veškeré komponenty byly zakoupeny na internetových e-shopech RPIshop.cz a Botland.com - ověřené a spolehlivé

<img src="images/parts.png" al
t="drawing" width="600px"/>

V projektu se k propojení jednotlivých komponent používá ekosystém GROVE od spol. seeed studio, díky kterému se do projektu dají zakomponovat další součásky bez potřeby jakéhokoli pájení(Pokud se nejedná o oficiální GROVE komponent tak se musí dopájet koncovka).

Pokud nechcete používat ekosystém GROVE, tak tento projekt lze zrealizovat i pomocí nepajivého pole či přímého spojení drátů.

## Tvoření projektu

   Se samotným nápadem přišel můj otec, když jsem se ho ptal co bych mohl udělat za projekt. Tento projekt se mi ih

## Postup Zapojení
### 1) Zapojíme Raspberry Pi Pico 2 WH do Grove Shield pro RPi Pico v1.0
   <img src="images/1.png" alt="drawing" width="600px"/>

   Pokud se později rozhodnete Raspberry z Grove Shield vyndat, musíte takto učinit s vysokou opatrností - hrozí zohnutí pinů. 

### 2) Propojíme relé s Grove Shield pro RPi Pico v1.0(D16)

   <img src="images/2.png" alt="drawing" width="600px"/>

   Zde si při zapojování dávejte pozor - propojovací kabely jsou křehké a jednotlivé kabely nejsou mezi koncovkami nijak chráněny, proto při příliž hrubém zacházení, namáhání či samotném zapojování hrozí přetrhnutí kabelů.

### 3) Napájíme adaptér Grove na pin na DS18B20

   <img src="images/teplomer konektory.png" alt="drawing" width="300px"/>
   <img src="images/konektor.png" alt="drawing" width="300px"/>

   <img src="images/pajeni.png" alt="drawing" width="600px"/>

   Při pájení musíme také dbát zvýšené pozornosti, jelikož adaptér má atypické rozložení pinů na staně pájení(napájecí 3v3 a signálový jsou prohozené). Zároveň plast pokrývající konce "pájecích" pinů je velmi náchilný na vysoké teploty a při pájení se plast může "uškvařit" a poté je konektor nepoužitelný.

### 4) Propojíme teploměr s Grove Shield pro RPi Pico v1.0(D20)

   <img src="images/3.png" alt="drawing" width="600px"/>

### 5) Finální podoba

   Po zapojení všech komponent dle návodu by váš výsledek měl vypadat nějak takto :D.

   <img src="images/4.png" alt="drawing" width="600px"/>

   1) Grove Shield pro RPi Pico v1.0
   2) Raspberry Pi Pico 2 WH
   3) Grove - Relé
   4) Teplotní čidlo DS18B20
   5) Adaptér Grove na pin

## Věci do budoucna

## Odkazy






https://randomnerdtutorials.com/raspberry-pi-pico-ds18b20-micropython/
https://wiki.seeedstudio.com/Grove_System/
https://wiki.seeedstudio.com/One-Wire-Temperature-Sensor-DS18B20/
