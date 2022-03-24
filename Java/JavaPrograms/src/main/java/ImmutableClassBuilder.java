package src.main.java;

public class ImmutableClassBuilder {
    private String name;
    private int value;

    public ImmutableClassBuilder setName(String name) {
        this.name = name;
        return this;
    }

    public ImmutableClassBuilder setValue(int value) {
        this.value = value;
        return this;
    }

    public ImmutableClass createImmutableClass() {
        return new ImmutableClass();
    }
}