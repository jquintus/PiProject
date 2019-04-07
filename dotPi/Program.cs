using System;
using System.Threading;
using System.Device.Gpio;

namespace dotPi
{
    // https://www.hanselman.com/blog/InstallingTheNETCore2xSDKOnARaspberryPiAndBlinkingAnLEDWithSystemDeviceGpio.aspx
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            using (var controller = new GpioController(PinNumberingScheme.Logical))
            {
                var pin = 24;
                var lightTime = 300;
                controller.OpenPin(pin, PinMode.Output);
                for(int i = 0; i < 10; i++)
                {
                    Console.WriteLine("high");
                    controller.Write(pin, PinValue.High);
                    Thread.Sleep(lightTime);

                    Console.WriteLine("low");
                    controller.Write(pin, PinValue.Low);
                    Thread.Sleep(lightTime);
                }
           }
        }
    }
}
