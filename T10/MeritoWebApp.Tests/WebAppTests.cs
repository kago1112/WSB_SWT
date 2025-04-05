using Xunit;

namespace MeritoWebApp.Tests;

public class WebAppTests
{
    [Fact]
    public void Test1()
    {
        Assert.True(true);
    }
}

public class HomeControllertests
{
    [Fact]
    public void Test_HelloWorld()
    {
        Assert.Equal("Hello World!", "Hello World!");
    }
}