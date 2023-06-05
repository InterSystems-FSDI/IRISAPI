/// My first class
Class Demo.Person Extends (%Persistent, %Library.Populate)
{

/// Person's name
Property Name As %String [ Required ];

/// Phone number
Property Phone As %String;

/// Age
Property Age As %Integer;

/// This is the sum of two integers
ClassMethod Sum(A As %Integer = 0, B As %Integer = 0) As %Integer
{
  set result = A + B
  return result
}

/// Print out information 
Method Print() As %Status
{
  write !, "This person is named ", ..Name,"."
  write !, ..Name, "’s phone number is", ..Phone,"."
  write !, ..Name, " is ", ..Age, " years old."
}

/// Planet
Parameter PLANET = "Earth";

Storage Default
{
<Data name="PersonDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>Name</Value>
</Value>
<Value name="3">
<Value>Phone</Value>
</Value>
<Value name="4">
<Value>Age</Value>
</Value>
</Data>
<DataLocation>^Demo.PersonD</DataLocation>
<DefaultData>PersonDefaultData</DefaultData>
<IdLocation>^Demo.PersonD</IdLocation>
<IndexLocation>^Demo.PersonI</IndexLocation>
<StreamLocation>^Demo.PersonS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
