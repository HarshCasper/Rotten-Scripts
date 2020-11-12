@extends('layouts.app')

@section('content')
<div class="container">
    <div class="card p-4">
        <h4 class="font-weight-bold text-primary">Create Category</h4>
        <form method="POST" action="{{ route('category.store') }}">
            @csrf
            <div class="form-group">
                <label for="username">Category name</label>
                <input type="text" class="form-control" name="name" placeholder="category name" required>
            </div>
            <div class="form-group">
                <input type="submit" class="btn btn-primary form-control" value="Add">
            </div>
        </form>
    </div>
</div>
@endsection